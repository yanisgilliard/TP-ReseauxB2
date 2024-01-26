import socket
import os


def serve_file(filepath):
    if not os.path.exists(filepath):
        return "HTTP/1.1 404 NOT FOUND\n\nFile Not Found".encode()

    with open(filepath, "rb") as file:
        content = file.read()
        response = "HTTP/1.1 200 OK\n\n".encode() + content
        return response


def start_server(port=13337):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    server_socket.listen()

    print(f"Serveur démarré, écoute sur {port}...")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            request = conn.recv(1024).decode("utf-8")
            uri = request.split(" ")[1]

            if uri == "/":
                uri = "/index.html"

            response = serve_file("www" + uri)
            conn.sendall(response)

            filepath = "www" + uri
            print(f"Tentative d'accès au fichier : {filepath}")


if __name__ == "__main__":
    start_server()
