import requests # Import requests library
from config.config import BASE_URL  # Import BASE_URL from config.py
from config.api_request_keys import API_KEY  # Import API_KEY from api_request_keys.py

# Function to validate phone number using an external API
def validate_phone_number(number):
    url = f"{BASE_URL}/api/validate"  # Use the BASE_URL from config.py
    params = {
        "number": number,
        "access_key": API_KEY  # Use the API_KEY from config.py
    }
    response = requests.get(url, params=params)
    
    # Printing details for debugging (optional)
    print(f"\n[API] Request URL: {response.url}")
    print(f"[API] Status Code: {response.status_code}")
    print(f"[API] Response JSON: {response.json()}")
    
    return response
