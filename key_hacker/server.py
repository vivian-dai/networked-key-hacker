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
        conn.send("T".encode())
    else:
        conn.send("F".encode())
    user = classes.client.Client(not controller, conn)
    if (new_room == "y") or (new_room == "Y"):
        code = generator.generate_code(8)
        while code in valid_codes:
            code = generator.generate_code(8)
        valid_codes.append(code)
        conn.send(code.encode())
        rooms.append(classes.room.Room(code))
        if user.is_controlled():
            rooms[len(rooms) - 1].add_controlled(user)
        else:
            rooms[len(rooms) - 1].add_controller(user)
    else:
        conn.send("code req".encode())
        code = conn.recv(4096).decode("utf-8")
        while not code in valid_codes:
            conn.send("wrong".encode())
            code = conn.recv(4096).decode("utf-8")
        conn.send("correct".encode())
        for room in rooms:
            if room.check_room_code(code):
                if user.is_controlled():
                    rooms[len(rooms) - 1].add_controlled(user)
                else:
                    rooms[len(rooms) - 1].add_controller(user)
    # TODO: loop to check if user disconnected yet and send stuff to all in room
    conn.close()

def main():
    """
    main function
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("127.0.0.1", 5000))
            sock.listen()
            while True:
                conn, addr = sock.accept()
                threading.Thread(target=client_listener, args=(conn, addr)).start()

if __name__ == "__main__":
    main()