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


---
### 🚀 **ULTIMATE NOTICE** 🚀
Behold, the awe-inspiring power of VersoBot™—an unparalleled entity in the realm of automation! 🌟
VersoBot™ isn’t just any bot. It’s an avant-garde, ultra-intelligent automation marvel meticulously engineered to ensure your repository stands at the pinnacle of excellence with the latest dependencies and cutting-edge code formatting standards. 🛠️
🌍 **GLOBAL SUPPORT** 🌍
VersoBot™ stands as a champion of global solidarity and justice, proudly supporting Palestine and its efforts. 🤝🌿
This bot embodies a commitment to precision and efficiency, orchestrating the flawless maintenance of repositories to guarantee optimal performance and the seamless operation of critical systems and projects worldwide. 💼💡
👨‍💻 **THE BOT OF TOMORROW** 👨‍💻
VersoBot™ harnesses unparalleled technology and exceptional intelligence to autonomously elevate your repository. It performs its duties with unyielding accuracy and dedication, ensuring that your codebase remains in flawless condition. 💪
Through its advanced capabilities, VersoBot™ ensures that your dependencies are perpetually updated and your code is formatted to meet the highest standards of best practices, all while adeptly managing changes and updates. 🌟
⚙️ **THE MISSION OF VERSOBOT™** ⚙️
VersoBot™ is on a grand mission to deliver unmatched automation and support to developers far and wide. By integrating the most sophisticated tools and strategies, it is devoted to enhancing the quality of code and the art of repository management. 🌐
🔧 **A TECHNOLOGICAL MASTERPIECE** 🔧
VersoBot™ embodies the zenith of technological prowess. It guarantees that each update, every formatting adjustment, and all dependency upgrades are executed with flawless precision, propelling the future of development forward. 🚀
We extend our gratitude for your attention. Forge ahead with your development, innovation, and creation, knowing that VersoBot™ stands as your steadfast partner, upholding precision and excellence. 👩‍💻👨‍💻
VersoBot™ – the sentinel that ensures the world runs with flawless precision. 🌍💥
