import os
import sys
from pathlib import Path

# Add repository root to sys.path to allow: from app import ...
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest

from starlette.testclient import TestClient
from app.main import app



@pytest.fixture
def client_no_raise():
    """Fixture to create a TestClient instance without raising server exceptions.

    This fixture is useful for tests that expect HTTP 500 responses instead of
    exceptions being raised directly by FastAPI during request handling.

    Yields:
        TestClient: A FastAPI TestClient with `raise_server_exceptions` disabled.
    """
    with TestClient(app, raise_server_exceptions=False) as client:
        yield client


def pytest_collection_modifyitems(config, items):
    """
    Automatically skip gpu_cuda/gpu_mps tests if the hardware is not available.

    Args:
        config: The pytest config object.
        items: List of collected test items.
    """
    try:
        import torch
    except Exception:
        torch = None

    cuda_available = bool(torch and torch.cuda.is_available())
    mps_available = bool(
        torch and getattr(torch.backends, "mps", None) and torch.backends.mps.is_available()
    )

    skip_cuda = pytest.mark.skip(reason="CUDA not available")
    skip_mps = pytest.mark.skip(reason="MPS not available")

    for item in items:
        if "gpu_cuda" in item.keywords and not cuda_available:
            item.add_marker(skip_cuda)
        if "gpu_mps" in item.keywords and not mps_available:
            item.add_marker(skip_mps)


def pytest_addoption(parser):
    """
    Add custom command-line option to enable running slow tests.

    Args:
        parser: The pytest parser object.
    """
    parser.addoption(
        "--run-slow",
        action="store_true",
        default=False,
        help="run slow tests"
    )


@pytest.fixture(autouse=True)
def _skip_slow(request):
    """
    Automatically skip tests marked as 'slow' unless --run-slow is specified.

    Args:
        request: The pytest request object for the current test.
    """
    if request.node.get_closest_marker("slow") and not request.config.getoption("--run-slow"):
        pytest.skip("use --run-slow to run this test")


