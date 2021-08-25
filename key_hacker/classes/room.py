"""
Class for Room
"""
class Room:
    def __init__(self, room_id):
        """
        Constructor for a room

        Args:
            room_id (string): the room's ID which is also its invite code
        """
        self.room_id = room_id
        self.controlled = []
        self.controller = []
        self.users = []

    def add_controlled(self, user):
        """
        Adds someone who will be getting their keyboard controlled

        Args:
            user (client.Client): the client to add
        """
        self.controlled.append(user)
        self.users.append(user)

    def add_controller(self, user):
        """
        Adds someone who will be controlling another's keyboard

        Args:
            user (client.Client): the client to add
        """
        self.controller.append(user)
        self.users.append(user)

    def check_room_code(self, code):
        """
        This isn't secure but that's ok

        Args:
            code (string): The code

        Returns:
            boolean: True if this is the same as the invite code, False otherwise
        """
        return self.room_id == code
