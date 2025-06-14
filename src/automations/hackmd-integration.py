import httpx
from datetime import datetime

# Configurações da API do HackMD
HACKMD_API_TOKEN = "meu_token"

BASE_URL = "https://api.hackmd.io/v1/"
headers = {
    "Authorization": f"Bearer {HACKMD_API_TOKEN}",
    "Content-Type": "application/json"
}

# Data atual no formato DD/MM/YYYY
today = datetime.now().strftime("%d/%m/%Y")
note_title = f"Reunião pybr2025 {today}"

async def create_public_note():
    try:
        async with httpx.AsyncClient() as client:
            # 1. Criar a nota com permissões públicas
            create_response = await client.post(
                f"{BASE_URL}notes",
                headers=headers,
                json={
                    "title": note_title,
                    "content": f"# {note_title}\n\n## Pauta\n- Item 1\n- Item 2\n\n## Ações\n- [ ] Tarefa 1",
                    "readPermission": "guest",  # Todos podem ler
                    "writePermission": "guest"  # Todos podem editar
                }
            )
            create_response.raise_for_status()

            note_data = create_response.json()
            note_id = note_data["id"]
            note_url = f"https://hackmd.io/{note_id}"

            print(f"✅Nota criada com sucesso!")
            print(f"📌 Título: {note_title}")
            print(f"🔗 Link de acesso: {note_url}")

    except httpx.HTTPStatusError as e:
        print(f"Erro na API: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")


# Executar
import asyncio

asyncio.run(create_public_note())
