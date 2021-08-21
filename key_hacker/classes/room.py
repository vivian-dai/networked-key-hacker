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
        self.controllee = []
        self.users = []