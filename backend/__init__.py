# Frameit-Application/backend/__init__.py

# Centralized imports for commonly used modules
from backend.core.logger import logger
from .core.database import engine

# Package metadata
__version__ = "1.0.0"

# You can add global initialization here, e.g., database or logger setup.
logger.info("Backend package initialized successfully.")
