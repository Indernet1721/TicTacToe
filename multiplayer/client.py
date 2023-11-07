import socket

#git test

SERVER = "192.168.56.1"
PORT = 5050
HEADER_SIZE = 16 # number of bytes of the header
ENCODING = "utf-8"
DISCONNECT_MSG = "-connection_lost"

world_data = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]



def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER, PORT))
    except:
        print("An error occured while trying to connect to the server.\nPlease make sure that the server is running and there are less than two clients connected.")
        return

    send_msg(client, world_data)


def send_msg(client, msg):
    message = str(msg).encode(ENCODING)
    header = str(len(message)).encode(ENCODING)
    header += b" " * (HEADER_SIZE - len(header))

    client.send(header)
    client.send(message)



if __name__ == "__main__": main() 
