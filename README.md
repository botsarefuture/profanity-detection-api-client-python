# Profanity Detection API Python Client

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)

A Python client for LuovaClub's Profanity Detection API, designed to identify and analyze profanity in text.

## Usage

### Example

1. Open `ProfanityDetectionClient.py`.
2. Run the example script:

   ```bash
   python ProfanityDetectionClient.py
   ```

### Integration

To integrate the Profanity Detection API client into your project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/profanity-detection-api-client-python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd profanity-detection-api-client-python
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Open `ProfanityDetectionClient.py`.
5. Run the example script or incorporate the `ProfanityDetectionClient` class into your project.

```python
from ProfanityDetectionClient import ProfanityDetectionClient

# Initialize the Profanity Detection API client with the API base URL
api_url = 'https://profanity.luova.club/api'
profanity_client = ProfanityDetectionClient(api_url)

# Example text to check for profanity
text_to_check = "This is a test sentence with no profanity."

# Detect profanity in the provided text
result = profanity_client.detect_profanity(text_to_check)

# Print the result
if result:
    if result['profanity_detected']:
        print("Profanity detected in the provided text.")
    else:
        print("No profanity detected in the provided text.")
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or issues, please contact the developer:
- Email: vuoreol@gmail.com

## API Documentation

For detailed API documentation, refer to the [Profanity Detection API Swagger Documentation](https://github.com/botsarefuture/profanity-detector-api).
