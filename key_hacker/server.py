import socket
import threading
import classes
import modules.generate as generator

PORT = 5000

valid_codes = []
rooms = []

def client_listener(conn, addr):
    """
    Listens to clients and responds to requests

    Args:
        conn (socket.socket): the client connection
        addr (tuple): where the connection is from 
    """
    print(f"connection from {addr}")
    controller = False
    control = conn.recv(4096).decode("utf-8")
    new_room = conn.recv(4096).decode("utf-8")
    if (control == "y") or (control == "Y"):
        controller = True
    conn.send(controller.encode())
    user = classes.client.Client(not controller, conn)
    if (new_room == "y") or (new_room == "Y"):
        code = generator.generate_code(8)
        while not code in valid_codes:
            code = generator.generate_code(8)
        valid_codes.append(code)
        conn.send(code.encode())
    else:
        conn.send("code req")
    while True:
        msg = conn.recv(4096).decode("utf-8")
        print(msg)

def main():
    """
    main function
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("127.0.0.1", 5000))
            sock.listen()
            conn, addr = sock.accept()
            threading.Thread(target=client_listener, args=(conn, addr)).start()

if __name__ == "__main__":
    main()