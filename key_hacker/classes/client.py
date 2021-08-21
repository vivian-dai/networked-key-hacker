"""
Class for server to store client types and data etc.
"""

class Client:
    """
    Client class
    """

    def __init__(self, controlled, conn):
        """
        Constructor

        Args:
            controlled (boolean): Whether or not this client is being controlled
            conn (socket.socket): the connection for this client
        """
        self.controlled = controlled
        self.conn = conn

    def is_controlled(self):
        return self.controlled

    def get_connection(self):
        return self.conn