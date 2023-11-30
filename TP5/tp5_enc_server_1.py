import socket 
import sys

def read_message(conn):
    header = conn.recv(2)
    message_size = int.from_bytes(header, byteorder='big')

    message = conn.rcv(message_size).decode() 

    end_seq = conn.recv(1)
    if end_seq != b'\x00':
        raise ValueError("Séquence de fin de message incorrecte")

    return message 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.1.2.12', 13337))
s.listen(1)
conn, addr = s.accept()

print("Connecté à:", addr)

try:
    hello_message = read_message(conn)
    print(f"Reçu : {hello_message}")
    conn.send(b'Hello')

    calculation = read_message(conn)
    print(f"Calcul reçu : {calculation}")

    try:
        result = str(eval(calculation))
        conn.send(result.encode())
    except Exception as e:
        error_msg = f"Erreur : {e}"
        conn.send(error_msg.encode())
finally : 
    conn.close()
    s.close()