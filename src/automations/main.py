import httpx
import os
from urllib.parse import quote

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ISSUE_TITLE = os.getenv("ISSUE_TITLE")
ISSUE_URL = os.getenv("ISSUE_URL")
COMMENT_USER = os.getenv("COMMENT_USER")
COMMENT_BODY = os.getenv("COMMENT_BODY")
COMMENT_URL = os.getenv("COMMENT_URL")
CHAT_ID = "-1002120660974"
THREAD_ID = 1888
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"


def escape_markdown(text):
    escape_chars = '_*[]()~`>#+-=|{}.!'
    return ''.join(f'\\{char}' if char in escape_chars else char for char in text)

def main():
    issue_title_escaped = escape_markdown(ISSUE_TITLE)
    comment_user_escaped = escape_markdown(COMMENT_USER)
    comment_body_escaped = escape_markdown(COMMENT_BODY)

    message = f"""
Novo [comentário]({COMMENT_URL}) de *{comment_user_escaped}* na issue [{issue_title_escaped}]({ISSUE_URL})

*Texto do comentário*:
{comment_body_escaped}
""".strip()
    params = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": message,
        "parse_mode": "MarkdownV2"
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
