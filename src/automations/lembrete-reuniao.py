import httpx
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


CHAT_ID = "-1002120660974"
THREAD_ID = 1888

# Grupo de teste
# CHAT_ID = "-1002354441960"
# THREAD_ID = 2

# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

def main():
    message = f"""
Olá meu povo, lembrete para nossa reunião semanal hoje às 18:30
O link para entrar na chamada é esse:
https://meet.google.com/ons-mudm-boj

Escrevam suas pautas para a reunião respondendo essa mensagem o/
"""
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
