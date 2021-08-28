import pygame

def setup():
    """
    Sets up pygame

    Returns:
        pygame.display: a screen to use for detecting things
    """
    pygame.init()
    pygame.display.set_caption(">:)")
    return pygame.display.set_mode((300, 200))

def controller(conn):
    screen = setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                conn.send("disconnect".encode())
                running = False
            elif event.type == pygame.KEYDOWN:
                conn.send(str(event.unicode).encode())
                conn.send("d".encode())
            elif event.type == pygame.KEYUP:
                conn.send(str(chr(event.key)).encode())
                conn.send("u".encode())
        pygame.display.flip()
    pygame.quit()
    
