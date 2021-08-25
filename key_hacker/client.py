import socket
import pygame

def input_connection_info():
    """
    gets the connection information

    Returns:
        tuple: ip and port
    """
    ip = input("enter your target IP: ")
    port = input("enter your target port: ")
    return (ip, int(port))

def setup():
    """
    setup function
    """
    try:
        with socket.create_connection(input_connection_info()) as sock:
            print("k time to do malicious stuff")
            sock.send(input("wanna control someone's keyboard? (y/n)").encode())
            sock.send(input("wanna create a new room? (y/n)").encode())
            controller = sock.recv(4096).decode("utf-8") == "T"
            code = sock.recv(4096).decode("utf-8")
            if code == "code req":
                sock.send(input("sauce join code :)").encode())
                resp = sock.recv(4096).decode("utf-8")
                while resp == "wrong":
                    sock.send(input("sauce join code :)").encode())
                    resp = sock.recv(4096).decode("utf-8")
                #TODO: code interfaces then open up an interface based on which it is
            
    except:
        print("rip something failed")

if __name__ == "__main__":
    setup()