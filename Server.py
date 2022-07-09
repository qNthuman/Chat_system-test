import socket,threading
ADDR = socket.gethostbyname(socket.gethostname())
PORT = 9698
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ENCODING  ="utf-8"

clients = []
nicknames = []

server.bind((ADDR,PORT))
server.listen()

def broad(msg):
    """SENDING MESSAGES TO ALL CLIENTS"""
    for client in clients:
        client.send(msg.encode(ENCODING))


def chat_room(conn):
    while True:
        try:
            msg = conn.recv(1024)
            broad(msg)
        except:
            ind = conn.index(clients)
            clients.remove(ind)
            nickname = nicknames[ind]
            nicknames.remove(nickname)
            broad(f"{nickname}left.".encode(ENCODING))
            conn.close()
            break


def setup():
    """TO SETUP THE SERVER"""
    while True:
        conn , addr = server.accept()
        print(f"Connected TO:{conn} addr:{addr}")
        nickname = conn.recv(1024)
        nickname = nickname.decode(ENCODING)
        # conn.sendall("nick".encode(ENCODING))
        broad(f"[{nickname} JOINED THE CHAT.]")
        nicknames.append(nickname)
        clients.append(conn)

        thread = threading.Thread(target=chat_room, args=conn)
        thread.start()

