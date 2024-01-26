import socket
import struct


def send_message(
    s,
    number1,
    operator,
    number2,
):
    message = struct.pack((">IcI", number1, operator.encode(), number2))
    print(f"packed message : {message}, Lenght : {len(message)}")
    s.send(struct.pack(">I", len(message)) + message)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.1.2.12", 13337))

number1 = int(input("Entrez le premier nombre: "))
operator = input("Entrez l'opérateur (+, -, *): ")
number2 = int(input("Entrez le second nombre: "))

send_message(s, number1, operator, number2)

result = s.recv(1024)
print("Result:", result.decode())

s.close
