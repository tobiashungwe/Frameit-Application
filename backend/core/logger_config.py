import logfire
import json
from pathlib import Path

# Load Logfire configuration
config_path = Path(__file__).parent / "logfire_config.json"
print(config_path)
with open(config_path, "r") as config_file:
    logfire_config = json.load(config_file)

# Configure Logfire using the loaded config
logfire.configure(**logfire_config)


# Instrument FastAPI or other components
def instrument_fastapi(app):
    logfire.instrument_fastapi(app)
