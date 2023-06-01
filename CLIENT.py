import requests
import time

def get_file_hash(owner, repo, nome_arquivo, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    get_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{nome_arquivo}"
    get_response = requests.get(get_url, headers=headers)
    get_data = get_response.json()
    sha = get_data["sha"]
    return sha

# Exemplo de uso
owner = "Grupo-OpenCV-BR"
repo = "tutoriais-tecnologia"
nome_arquivo = "requisitos.txt"
access_token = "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"

sha = get_file_hash(owner, repo, nome_arquivo, access_token)
print(f"Hash do arquivo: {sha}")
