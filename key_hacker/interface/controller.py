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
                #TODO: diffrentiate between keyup and keydown to send over both
        pygame.display.flip()
    pygame.quit()
