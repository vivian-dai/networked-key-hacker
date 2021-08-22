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
        """
        Whether or not the client is controlled

        Returns:
            boolean: True if controlled, False if controller
        """
        return self.controlled

    def get_connection(self):
        """
        Gets the connection

        Returns:
            socket.socket: the connection where everything happens
        """
        return self.conn