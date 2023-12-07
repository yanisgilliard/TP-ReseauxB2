import os
import requests

def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la récupération du contenu : {e}")
        return None

def write_content(content, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Le contenu a été écrit dans le fichier : {file_path}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'écriture du contenu dans le fichier : {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    content = get_content(url)

    if content:
        file_path = '/tmp/web_page'
        write_content(content, file_path)
    else:
        print("Impossible de récupérer le contenu de la page.")
