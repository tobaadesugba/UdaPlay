# Load in the OpenAI key and Tavily key.
# In the project folder, create a file named 'config.env'
# ensure your config.env file contains:
# OPENAI_API_KEY="your key"
# TAVILY_API_KEY="your key"
# OPENAI_BASE_URL="https://openai.vocareum.com/v1"

from dotenv import load_dotenv
import os

load_dotenv(".env")

assert os.getenv("OPENAI_API_KEY") is not None
assert os.getenv("TAVILY_API_KEY") is not None

OPENAI_BASE_URL = os.getenv(
    "OPENAI_BASE_URL",
    "https://openai.vocareum.com/v1"
)