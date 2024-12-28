# TODO: Make sure to update the logger with something that is more flexible so that i do not break the principle of DRY

import sys
import logfire
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from backend.core.database import Base, engine
from backend.infrastructure.controllers import (
    agent_controller,
    theme_controller,
    story_controller,
)

# Create all DB tables on startup (if you prefer)
Base.metadata.create_all(bind=engine)

# Configure Logfire before other imports
logfire.configure()
logfire.install_auto_tracing(
    modules=["backend"], min_duration=0.01, check_imported_modules="warn"
)

# Dynamically add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


# Initialize FastAPI app
app = FastAPI(title="FrameIt API", version="1.0.0")
logfire.instrument_fastapi(app)
logfire.info("Starting FastAPI application...")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (for swagger.json or other static content)
static_dir = Path(__file__).parent / "infrastructure" / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


# Include your controllers/routers
app.include_router(agent_controller.router, prefix="/api/agents", tags=["Agents"])
app.include_router(theme_controller.router, prefix="/api/themes", tags=["Themes"])
app.include_router(story_controller.router, prefix="/api/stories", tags=["Stories"])


@app.get("/health")
def health_check():
    """Health check endpoint to ensure the API is running."""
    logfire.info("Health check endpoint was called.")
    return {"status": "OK", "message": "API is up and running!"}
