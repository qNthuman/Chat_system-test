import socket
ADDR = "localhost"
PORT = 9698
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ENCODING = "utf-8"

client.connect((ADDR,PORT))
while True:
    msg = client.recv(1024).decode(ENCODING)
    if msg == "nick":
        name = input("Enter your nickname:")
        nickname = client.send(name).encode(ENCODING)