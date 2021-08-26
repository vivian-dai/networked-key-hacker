import pyautogui

def controlled(conn):
    running = True
    while running:
        msg = conn.recv(4096).decode()
        pyautogui.press(msg) #TODO: diffrentiate between keyup and keydown to send over both
