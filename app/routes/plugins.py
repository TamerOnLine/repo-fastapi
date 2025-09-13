from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, HTTPException, Request

from app.plugins import loader

router = APIRouter()


def _ensure_discovered(request: Request) -> None:
    """
    Ensure plugin registry and metadata are discovered and cached in app state.

    Args:
        request (Request): The incoming FastAPI request object.
    """
    if not hasattr(request.app.state, "plugin_registry") or not hasattr(request.app.state, "plugin_meta"):
        registry, meta = loader.discover(reload=False)
        request.app.state.plugin_registry = registry
        request.app.state.plugin_meta = meta


@router.get("/plugins", summary="List loaded plugins")
def list_plugins(request: Request) -> Dict[str, Any]:
    """
    List metadata of all loaded plugins.

    Args:
        request (Request): The incoming FastAPI request object.

    Returns:
        Dict[str, Any]: A dictionary containing the count and metadata of plugins.
    """
    _ensure_discovered(request)
    meta: Dict[str, Dict[str, Any]] = request.app.state.plugin_meta
    return {"count": len(meta), "plugins": meta}


@router.post("/plugins/{name}/{task}", summary="Run a task on a plugin")
def run_plugin_task(name: str, task: str, payload: Dict[str, Any], request: Request) -> Dict[str, Any]:
    """
    Execute a specific task on a given plugin.

    Args:
        name (str): The name of the plugin.
        task (str): The task to execute.
        payload (Dict[str, Any]): The task input payload.
        request (Request): The incoming FastAPI request object.

    Returns:
        Dict[str, Any]: The result of executing the task on the plugin.

    Raises:
        HTTPException: If the plugin is not found or task execution fails.
    """
    _ensure_discovered(request)
    registry = request.app.state.plugin_registry

    if name not in registry:
        raise HTTPException(status_code=404, detail=f"Plugin '{name}' not found")

    plugin = registry[name]
    payload = {"task": task, **payload}

    try:
        result = plugin.infer(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Infer error: {e!s}")

    return {"plugin": name, "result": result}
