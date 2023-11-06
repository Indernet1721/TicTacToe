import socket
import threading



PORT = 5050
HOST = socket.gethostbyname(socket.gethostname()) # get local ip
DISCONNECT_MSG = "-connection_lost"
HEADER_SIZE = 16 # number of bytes of the header
ENCODING = "utf-8"
MAX_CLIENTS = 2

current_clients = 0
world_data = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]



def main():
    global current_clients
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Listening on " + HOST + ":" + str(PORT))

    while current_clients < MAX_CLIENTS:
        conn, addr = server.accept() # blocking
        thread = threading.Thread(target=client_thread, args=(conn, addr))
        thread.start()
        current_clients += 1


def client_thread(conn, addr):
    print("new connection: " + str(addr))

    while True:
        msg_len = conn.recv(HEADER_SIZE).decode(ENCODING) # blocking    # get the size of the actual msg via this header msg
        if not msg_len: continue
        msg_len = int(msg_len)
        msg = conn.recv(msg_len).decode(ENCODING) # actual msg
        
        if(msg == DISCONNECT_MSG):
            conn.close()
            break
        
        print(addr, msg)



if __name__ == "__main__": main()
