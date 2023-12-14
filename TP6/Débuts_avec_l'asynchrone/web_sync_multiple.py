import os
import requests
import sys

def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la récupération du contenu de {url} : {e}")
        return None

def write_content(content, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Le contenu de la page a été écrit dans le fichier : {file_path}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'écriture du contenu dans le fichier : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    for url in urls:
        file_name = '/tmp/web_' + url.replace('https://', '').replace('/', '_')
        content = get_content(url)

        if content:
            write_content(content, file_name)
        else:
            print(f"Impossible de récupérer le contenu de la page {url}.")
