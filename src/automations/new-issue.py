import httpx
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ISSUE_TITLE = os.getenv("ISSUE_TITLE")
ISSUE_URL = os.getenv("ISSUE_URL")
ISSUE_NUMBER = os.getenv("ISSUE_NUMBER")
ISSUE_AUTHOR = os.getenv("ISSUE_AUTHOR")
ISSUE_BODY = os.getenv("ISSUE_BODY")

# CHAT_ID = "-1002120660974"
# THREAD_ID = 1888

CHAT_ID = "-1002354441960"
THREAD_ID = 2

# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

def main():
    message = f"""
Nova issue [{ISSUE_TITLE}]({ISSUE_URL}) criada por *{ISSUE_AUTHOR}* 

*Texto da issue*:
{ISSUE_BODY}
"""
    message = message.replace(" * ", "- ") # API do Telegram lida melhor com - do que com * pra listas
    params = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_notification": True
    }  
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = httpx.get(url, params=params)
    status_code = response.status_code
    if status_code != 200:
        print(f"Erro {status_code}: {response.json()}")
        raise Exception

if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/75116947/how-to-send-messages-to-telegram-using-python
# https://core.telegram.org/bots/api#sendmessage
# https://docs.github.com/en/webhooks/webhook-events-and-payloads?actionType=opened#issues
# https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#issues
