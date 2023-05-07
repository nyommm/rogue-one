"""
entity - This module defines the Entity base class
"""
from typing import Tuple


class Entity:
    """
    The base class to represent entities/objects that appear in the game.
    For example, the player, the enemies, and items etc.
    """

    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def translate(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
