import socket
import re


def create_header_and_message(msg):
    header = len(msg).to_bytes(2, byteorder="big")
    full_message = header + msg.encode() + b"\x00"
    return full_message


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.1.2.12", 13337))

s.send(create_header_and_message)("Hello")

data = s.recv(1024)
print(data.decode())

msg = input("Calcul à envoyer (operations autorisées : +, -, *):")
while not re.match(r"^\d+[\+\-\*]\d+$", msg):
    print("Format invalide, veuillez entrer une expression correcte.")
    msg = input("Calcul à envoyer: ")

s.send(create_header_and_message)

result_data = s.recv(1024)
print(result_data.decode())

s.close
