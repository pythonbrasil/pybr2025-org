import os
import re
import httpx
from urllib.parse import quote

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ISSUE_TITLE = os.getenv("ISSUE_TITLE")
ISSUE_URL = os.getenv("ISSUE_URL")
COMMENT_USER = os.getenv("COMMENT_USER")
COMMENT_BODY = os.getenv("COMMENT_BODY")
COMMENT_URL = os.getenv("COMMENT_URL")

# carrega a lista de usuários do Telegram a partir da variável de ambiente TELEGRAM_USERS_MAP
# ex: @github-user:@telegram_user,@github-user2:@telegram_user2,...

TELEGRAM_USERS_MAP = os.getenv("TELEGRAM_USERS_MAP")

# Gera o mapa de usuários do Telegram a partir da variável de ambiente
TELEGRAM_USERS_MAP = dict(
    user.split(":") for user in TELEGRAM_USERS_MAP.split(",") if ":" in user
)

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

    # Verifica se o mapa de usuários do Telegram não está vazio para realizar a substituição
    if(TELEGRAM_USERS_MAP):

        # percorre cada palavra do corpo do comentário
        for palavra in COMMENT_BODY.split():

            # se a palavra começa com @ e tem mais de 3 caracteres, verifica se está no mapa de usuários do Telegram
            if palavra.startswith("@") and len(palavra) > 3 and palavra in TELEGRAM_USERS_MAP.keys():

                # se a palavra está no mapa de usuários do Telegram, substitui pelo id do usuário do Telegram

                telegram_user = re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', TELEGRAM_USERS_MAP[palavra])
                message += f"\n{telegram_user}"

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
