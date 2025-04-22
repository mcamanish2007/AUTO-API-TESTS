# Project Name

## Overview
This project includes API tests that validate phone numbers.

## Test Cases

| **Test Case ID** | **Test Description**                                     | **Input**                   | **Expected Result**                                                                                          | **Status**   |
|------------------|-----------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------|--------------|
| TC-001           | Verify that a valid phone number is correctly validated.  | `"14158586273"` (valid)     | The response should indicate that the phone number is valid. The `valid` key should be `True`.                | Passed       |
| TC-002           | Verify that an invalid phone number format returns false. | `"12345"` (invalid format)  | The response should indicate that the phone number is invalid. The `valid` key should be `False`.             | Passed       |
| TC-003           | Verify that a phone number that's too short returns false. | `"1"` (too short)           | The response should indicate that the phone number is invalid. The `valid` key should be `False`.             | Passed       |
| TC-004           | Verify that a phone number with non-numeric characters returns false. | `"abc123def456"` (non-numeric) | The response should indicate that the phone number is invalid. The `valid` key should be `False`.             | Passed       |
| TC-005           | Verify that a phone number with an incorrect country code returns false. | `"+9991234567890"` (invalid country code) | The response should indicate that the phone number is invalid. The `valid` key should be `False`.             | Passed       |

## How to Run Tests

1. Install dependencies: `pip install -r requirements.txt`
3. Add a .env file at the root folder and define API_KEY="****************************" inside it.
2. Run the tests: `pytest tests/`
