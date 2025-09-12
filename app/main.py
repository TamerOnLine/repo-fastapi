from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import get_settings

settings = get_settings()

# Template and static file paths
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI(title="NeuroServe")

# Serve static files under /static if available
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    """
    Serve the homepage template.

    Args:
        request (Request): The HTTP request object.

    Returns:
        TemplateResponse: Rendered index.html template.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health", response_class=JSONResponse)
def health():
    return {"status": "ok"}

@app.get("/env", response_class=JSONResponse)
def env():
    return settings.summary()


# Include routers for CUDA and file uploads
