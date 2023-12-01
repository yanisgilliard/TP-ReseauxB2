import requests 

def send_get_request(url):
    try:
        response = requests.get(url)
        print(f"Statut de la réponse : {response.status_code}")
        print("Contenu de la réponse :")
        print(response.text)
    except requests.exceptions.RequestExecption as e:
        print(f"Erreur lors de la requête : {e}")

if __name__ == "__main__":
    url = input("Entrez l'url pour envoyer une requête GET :")
    send_get_request(url) 