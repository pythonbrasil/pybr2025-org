import httpx
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ISSUE_TITLE = os.getenv("ISSUE_TITLE")
ISSUE_URL = os.getenv("ISSUE_URL")
COMMENT_USER = os.getenv("COMMENT_USER")
COMMENT_BODY = os.getenv("COMMENT_BODY")
COMMENT_URL = os.getenv("COMMENT_URL")
CHAT_ID = "-1002120660974"
THREAD_ID = 1888
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

def main():
    message = f"""
Novo [comentário]({COMMENT_URL}) de *{COMMENT_USER}* na issue [{ISSUE_TITLE}]({ISSUE_URL})

*Texto do comentário*:
{COMMENT_BODY}
"""
    message = message.replace(" * ", "- ") # API do Telegram lida melhor com - do que com * pra listas
    params = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": message,
        "parse_mode": "Markdown"
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
# https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#issue_comment
# https://docs.github.com/en/webhooks/webhook-events-and-payloads?actionType=created#issue_comment
