import os
from dotenv import load_dotenv

# Load environment variables from .pre-commit run --all-filesenv file
load_dotenv()


class ModelConfig:
    # Access the Groq API key
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    BRAVE_API_KEY = os.getenv("BRAVE_API_KEY", "your_default_brave_api_key")
