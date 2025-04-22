# config/api_request_keys.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access API key
API_KEY = os.getenv("API_KEY")

# Print the API key in a masked format, showing only the first 4 characters
masked_api_key = f"{API_KEY[:4]}****"  # Show first 4 characters, then mask with asterisks

print(f"API_KEY: {masked_api_key}")
