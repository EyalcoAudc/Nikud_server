import requests
import json


def send_request(text, url="http://127.0.0.1:5000/predict"):
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"text": text})

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    sample_text = "האם בתאריך עשרים וחמישה ביוני, ביום שני, בשעה ארבע ארבעים וחמש, במרפאה ברחוב הנביאים 2, חיפה, יתאים לכם תור אצל דוקטור אביטל, מומחה לרפואת עיניים?"
    send_request(sample_text)