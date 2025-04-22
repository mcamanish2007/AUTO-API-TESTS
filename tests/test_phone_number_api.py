import pytest # Import pytest for testing
from request.api_request import validate_phone_number  # Import the function
from utils import response_validator  # Import the custom assertion functions

# 1. Positive Test Case for Valid Phone Number
@pytest.mark.parametrize("phone_number", ["14158586273"])  # Valid phone number
def test_validate_phone_number_valid(phone_number):
    """
    Test that fetching a valid user returns status 200 and correct structure.
    """
    response = validate_phone_number(phone_number)

    # Validate response status code
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    response_json = response.json()

    # Custom assertions for keys using response_validator module
    response_validator.assert_key_in_response(response_json, "valid", "Response does not contain 'valid' key")
    response_validator.assert_key_type(response_json, "valid", bool, "'valid' key should be a boolean value")
    response_validator.assert_key_value(response_json, "valid", True, "Expected 'valid' to be True")

    # Further custom assertions for other response fields
    response_validator.assert_key_in_response(response_json, "number", "Response does not contain 'number' key")
    response_validator.assert_key_in_response(response_json, "country_name", "Response does not contain 'country_name' key")
    response_validator.assert_key_in_response(response_json, "carrier", "Response does not contain 'carrier' key")

    print(f"Phone number {phone_number} is valid. Response: {response_json}")

# 2. Negative Test Case for Invalid Phone Number (incorrect format)
@pytest.mark.parametrize("phone_number", ["12345"])  # Invalid phone number format (too short)
def test_validate_phone_number_invalid_format(phone_number):
    """
    Test that an invalid phone number format returns valid: False.
    """
    response = validate_phone_number(phone_number)

    # Validate response status code
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    response_json = response.json()

    # Custom assertions for invalid phone numbers
    response_validator.assert_key_value(response_json, "valid", False, "Expected 'valid' to be False for invalid number format")

    print(f"Phone number {phone_number} is invalid. Response: {response_json}")

# 3. Negative Test Case for Too Short Phone Number
@pytest.mark.parametrize("phone_number", ["1"])  # Too short phone number
def test_validate_phone_number_too_short(phone_number):
    """
    Test that a phone number that's too short returns valid: False.
    """
    response = validate_phone_number(phone_number)

    # Validate response status code
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    response_json = response.json()

    # Custom assertions for invalid short phone numbers
    response_validator.assert_key_in_response(response_json, "valid", "Response does not contain 'valid' key")
    response_validator.assert_key_value(response_json, "valid", False, "Expected 'valid' to be False for short phone number")
    
    print(f"Phone number {phone_number} is too short. Response: {response_json}")

# 4. Negative Test Case for Phone Number with Non-Numeric Characters
@pytest.mark.parametrize("phone_number", ["abc123def456"])  # Non-numeric characters in the phone number
def test_validate_phone_number_with_non_numeric(phone_number):
    """
    Test that a phone number with non-numeric characters returns valid: False.
    """
    response = validate_phone_number(phone_number)

    # Validate response status code
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    response_json = response.json()

    # Custom assertions for phone numbers with non-numeric characters
    response_validator.assert_key_in_response(response_json, "valid", "Response does not contain 'valid' key")
    response_validator.assert_key_value(response_json, "valid", False, "Expected 'valid' to be False for non-numeric phone number")
    
    print(f"Phone number {phone_number} contains non-numeric characters. Response: {response_json}")

# 5. Negative Test Case for Incorrect country code
@pytest.mark.parametrize("phone_number", ["+9991234567890"])  # Incorrect country code
def test_validate_phone_number_invalid_country_code(phone_number):
    """
    Test that a phone number with an invalid country code returns valid: False.
    """
    response = validate_phone_number(phone_number)

    # Validate response status code
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    response_json = response.json()

    # Custom assertions for phone numbers with an incorrect country code
    response_validator.assert_key_value(response_json, "valid", False, "Expected 'valid' to be False for phone number with invalid country code")


    # Printing out the response to debug or inspect
    print(f"Phone number {phone_number} has an invalid country code. Response: {response_json}")