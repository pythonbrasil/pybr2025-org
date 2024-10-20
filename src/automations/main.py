import httpx
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ISSUE_TITLE = os.getenv("ISSUE_TITLE")
#COMMENT_USER = os.getenv("COMMENT_USER_NAME")
COMMENT_BODY = os.getenv("COMMENT_BODY")
COMMENT_URL = os.getenv("COMMENT_URL")
CHAT_ID = "-1002120660974"
THREAD_ID = 1888
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

def main():
    message = f"""
    Novo comentário na issue {ISSUE_TITLE}
Link do comentário: {COMMENT_URL}
Texto do comentário: {COMMENT_BODY}
"""
    params = {
        "chat_id": CHAT_ID,
        "text": message,
        "message_thread_id": THREAD_ID,
        "disable_notification": True
    }    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    httpx.get(url, params=params)

if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/75116947/how-to-send-messages-to-telegram-using-python
# https://core.telegram.org/bots/api#sendmessage
# https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#issue_comment
# https://docs.github.com/en/webhooks/webhook-events-and-payloads?actionType=created#issue_comment
