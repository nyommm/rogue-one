"""
actions - This module defines classes for user actions. For example, player movement, quiting etc.
"""


class Action:
    """This serves as the base class for user actions."""
    pass


class EscapeAction(Action):
    """This class represents the Esc key press used to quit the game."""
    pass


class MovementAction(Action):
    """
    This class represents the key press(es)
    used to move the player in the game world.
    """

    def __init__(self, dx: int, dy: int):
        super.__init__()
        self.dx = dx
        self.dy = dy
