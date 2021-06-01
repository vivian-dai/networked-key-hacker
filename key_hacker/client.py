import socket

def input_connection_info():
    """gets the connection information

    Returns:
        tuple: ip and port
    """
    ip = input("enter your target IP")
    port = input("enter your target port")
    return (ip, int(port))

def main():
    """ main function
    """
    try:
        with socket.create_connection(input_connection_info()) as sock:
            print("k time to do malicious stuff")

if __name__ == "__main__":
    main()