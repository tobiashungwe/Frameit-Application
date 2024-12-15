import logging
from logfire import LogfireHandler

logfire_handler = LogfireHandler(
    api_key="your_logfire_api_key"
)  # Replace with your Logfire API key
logger = logging.getLogger("multi_agent_system")
logger.setLevel(logging.INFO)
logger.addHandler(logfire_handler)
