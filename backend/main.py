# TODO: Make sure to update the logger with something that is more flexible so that i do not break the principle of DRY

import sys
import logfire
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from backend.core.logger import logger
from backend.core.database import Base, engine
from backend.infrastructure.controllers import (
    theme_controller,
    story_controller,
    translation_controller,
    user_controller,  # ADD THIS
)

# Create all DB tables on startup
Base.metadata.create_all(bind=engine)

# Configure Logfire
logfire.configure()
logfire.install_auto_tracing(
    modules=["backend"],
    min_duration=0.01,
    check_imported_modules="warn"
)
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# Initialize FastAPI
app = FastAPI(title="FrameIt API", version="1.0.0")
logfire.instrument_fastapi(app)
logfire.info("Starting FastAPI application...")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # adapt to your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (if needed)
static_dir = Path(__file__).parent / "infrastructure" / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Include your controllers/routers
app.include_router(theme_controller.router, prefix="/api/themes", tags=["Themes"])
app.include_router(story_controller.router, prefix="/api/stories", tags=["Stories"])
app.include_router(translation_controller.router, prefix="/api/translations", tags=["Translations"])
app.include_router(user_controller.router, prefix="/api/users", tags=["Users"])  # <--- Add user routes

@app.get("/health")
def health_check():
    """Health check endpoint to ensure the API is running."""
    logfire.info("Health check endpoint was called.")
    return {"status": "OK", "message": "API is up and running!"}
