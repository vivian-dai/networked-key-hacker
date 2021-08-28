import pyautogui

def controlled(conn):
    running = True
    while running:
        msg = conn.recv(4096).decode()
        cmd = conn.recv(4096).decode()
        if cmd == "d":
            pyautogui.keyDown(msg)
        elif cmd == "u":
            pyautogui.keyUp(msg)
