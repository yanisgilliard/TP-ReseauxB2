import socket
import os
import logging

LOG_FILE_PATH = "www/var/log/tp5/server.log"

os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def serve_file(filepath, client_address):
    if not os.path.exists(filepath):
        logging.warning(f"File not found: {filepath} requested by {client_address}")
        return "HTTP/1.1 404 NOT FOUND\n\nFile Not Found".encode()

    with open(filepath, "rb") as file:
        content = file.read()
        logging.info(f"File served: {filepath} to {client_address}")
        response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n".encode() + content
        return response


def start_server(port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    server_socket.listen(5)

    print(f"Serveur démarré, écoute sur le port {port}...")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            request = conn.recv(1024).decode("utf-8")
            uri = request.split(" ")[1]
            if uri == "/":
                uri = "/index.html"
            filepath = "www" + uri
            response = serve_file(filepath, addr)
            conn.sendall(response)


if __name__ == "__main__":
    start_server()
