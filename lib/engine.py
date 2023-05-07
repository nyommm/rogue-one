"""
engine - This module defines the Engine class
"""

from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from .actions import EscapeAction, MovementAction
from .entity import Entity
from .event_handler import EventHandler


class Engine:
    """
    The Engine class handles events and renders the game world.
    """

    def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity):
        self.player = player
        self.entities = entities
        self.event_handler = event_handler

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if isinstance(action, MovementAction):
                self.player.translate(action.dx, action.dy)
                continue
            if isinstance(action, EscapeAction):
                raise SystemExit()

    def render(self, console: Console, context: Context) -> None:
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)
        console.clear()
