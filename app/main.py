from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import get_settings
from app.core.errors import register_exception_handlers
from app.core.logging_ import setup_logging
from app.routes import plugins as plugins_routes

# Initialize settings and logging
settings = get_settings()
setup_logging()

# Set base directory and templates path
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Create FastAPI application instance
app = FastAPI(title=settings.APP_NAME)

# Mount static files directory
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Add CORS middleware with settings from config
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
)

# Register custom exception handlers
register_exception_handlers(app)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    """
    Serve the index HTML page.

    Args:
        request (Request): The incoming HTTP request.

    Returns:
        TemplateResponse: Rendered HTML template for the index page.
    """
    return templates.TemplateResponse("index.html", {"request": request, "title": settings.APP_NAME})


@app.get("/health")
def health():
    """
    Health check endpoint.

    Returns:
        dict: A simple status check response.
    """
    return {"status": "ok"}


@app.get("/env")
def env():
    """
    Return application environment summary.

    Returns:
        dict: Summary of environment settings.
    """
    return settings.summary()

# Include plugin routes
app.include_router(plugins_routes.router, tags=["plugins"])
