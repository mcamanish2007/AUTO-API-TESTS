# utils/response_validator.py

def assert_key_in_response(response_json, key, custom_message=None):
    """Asserts that a key exists in the response JSON with a custom error message."""
    assert key in response_json, custom_message or f"Response does not contain '{key}' key"

def assert_key_type(response_json, key, expected_type, custom_message=None):
    """Asserts that the type of the key in the response JSON is of expected type."""
    assert isinstance(response_json.get(key), expected_type), custom_message or f"Expected '{key}' to be of type {expected_type}, got {type(response_json.get(key))}"

def assert_key_value(response_json, key, expected_value, custom_message=None):
    """Asserts that the key in the response JSON has the expected value."""
    assert response_json.get(key) == expected_value, custom_message or f"Expected '{key}' to be '{expected_value}', got {response_json.get(key)}"

def validate_keys_in_response(response_json, expected_keys):
    """Checks if all expected keys are present in the response JSON."""
    missing_keys = [key for key in expected_keys if key not in response_json]
    assert not missing_keys, f"Missing keys in response: {', '.join(missing_keys)}"
    return True
