import socket,threading

ADDR = socket.gethostbyname(socket.gethostname())
PORT = 6969
ENCODING  ="utf-8"

clients = []
nicknames = []


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Buiding the server's socket
server.bind((ADDR,PORT))
server.listen()

def broad(msg):
    """SENDING MESSAGES TO ALL CLIENTS"""
    for client in clients:
        client.send(msg)

def handle(client):
    """TO HANDLE CLIENTS"""
    while True:
        try:
            message = client.recv(1024)
            broad(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broad(f"{nickname}left.".encode(ENCODING))
            client.close()
            break


def setup():
    """TO SETUP THE SERVER"""
    while True:
        client, addr = server.accept()
        print(f"connected with {addr}")
        client.send("nick".encode(ENCODING))
        nickname = client.recv(1024).decode(ENCODING)
        nicknames.append(nickname)
        clients.append(client)
        print(f"connected")

        broad(f"{nickname}  joined".encode(ENCODING))
        client.send(("connected").encode(ENCODING))

        thread  = threading.Thread(target=handle , args=(client,))
        thread.start()




print("started")
setup()