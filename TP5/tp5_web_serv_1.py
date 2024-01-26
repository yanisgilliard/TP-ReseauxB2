import socket


def start_server(port=13337):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    server_socket.listen()

    print(f"Serveur démarré, en attente de requête sur le port {port}")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connecté à {addr}")
            request = conn.recv(1024).decode("utf-8")
            print(f"Requête reçue: \n{request}")

            http_reponse = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<h1>Hello, je suis un serveur HTTP</h1>"

            conn.sendall(http_reponse.encode("utf-8"))


if __name__ == "__main__":
    start_server()
