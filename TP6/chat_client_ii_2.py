import socket


def main():
    host = "127.0.0.1"
    port = 8888

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hello")
        data = s.recv(1024)

        print(f"Reçu du serveur : {data.decode()}")


if __name__ == "__main__":
    main()
