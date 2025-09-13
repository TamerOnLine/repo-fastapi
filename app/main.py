import uuid

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import get_settings
from app.core.errors import register_exception_handlers
from app.core.logging_ import setup_logging
from app.routes import plugins as plugins_routes

# Initialize settings and logging
settings = get_settings()
setup_logging()

# Use settings paths (recommended)
templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))

# Create FastAPI application instance
app = FastAPI(title=settings.APP_NAME)

# Mount static files directory (from settings)
app.mount("/static", StaticFiles(directory=str(settings.STATIC_DIR)), name="static")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
)


# Middleware: unique request ID
class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        rid = request.headers.get("x-request-id") or uuid.uuid4().hex
        request.state.request_id = rid
        response = await call_next(request)
        response.headers["X-Request-ID"] = rid
        return response


app.add_middleware(RequestIDMiddleware)

# Register exception handlers
register_exception_handlers(app)


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": settings.APP_NAME})


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/env")
def env():
    return settings.summary()


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse(str(settings.STATIC_DIR / "favicon.ico"))


# Include plugin routes
app.include_router(plugins_routes.router, tags=["plugins"])
