import requests

# API_TOKEN = "YOUR_API_TOKEN"
API_TOKEN = "7493318142:AAGp9nDF9QD-VAFdZIxMJe5uzXHoiahdZoM"

def send_message(chat_id, message):
    url = f"https://api.telegram.org/bot{7493318142:AAGp9nDF9QD-VAFdZIxMJe5uzXHoiahdZoM}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    requests.post(url, json=data)

def main():
    chat_id = "YOUR_CHAT_ID"
    message = "Hello from IssueTrackerBot!"
    send_message(chat_id, message)

if __name__ == "__main__":
    main()