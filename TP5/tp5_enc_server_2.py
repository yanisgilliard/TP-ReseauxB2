import socket
import struct


def process_message(message):
    number1, operator, number2 = struct.unpack(">IcI", message)
    operator = operator.decode()
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    else:
        raise ValueError("Mauvais Operateur")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("10.1.2.12", 13337))
s.listen(1)
conn, addr = s.accept()

while True:
    try:
        raw_lenght = conn.recv(4)
        if not raw_lenght:
            break
        lenght = struct.unpack(">I", raw_lenght)[0]

        message = conn.recv(lenght)
        print(f"Message Reçu: {message}, Lenght: {lenght}")
        result = process_message(message)

        conn.send(str(result).encode())

    except Exception as e:
        print(f"Erreur: {e}")
        break

conn.close()
