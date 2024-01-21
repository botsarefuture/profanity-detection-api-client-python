import requests

class ProfanityDetectionClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def detect_profanity(self, text, language='en'):
        endpoint = '/detect-profanity/'
        url = self.base_url + endpoint

        payload = {
            'text': text,
            'language': language
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

# Example usage:
if __name__ == "__main__":
    api_url = 'https://profanity.luova.club/api'
    profanity_client = ProfanityDetectionClient(api_url)

    text_to_check = "This is a test sentence with no profanity."
    result = profanity_client.detect_profanity(text_to_check)

    if result:
        if result['profanity_detected']:
            print("Profanity detected in the provided text.")
        else:
            print("No profanity detected in the provided text.")
