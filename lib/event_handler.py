"""
event_handler - This module defines the EventHandler class
"""

import tcod.event
from typing import Optional
from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    """This class overrides methods that handle events dispatched by tcod"""

    def ev_quit(self, evt: tcod.event.Quit) -> Optional[Action]:
        """Quit the game"""
        raise SystemExit()

    def ev_keydown(self, evt: tcod.event.KeyDown) -> Optional[Action]:
        """Handle key down event"""
        key = evt.sym

        if key == tcod.event.K_UP:
            return MovementAction(dx=0, dy=-1)
        if key == tcod.event.K_DOWN:
            return MovementAction(dx=0, dy=1)
        if key == tcod.event.K_LEFT:
            return MovementAction(dx=-1, dy=0)
        if key == tcod.event.K_RIGHT:
            return MovementAction(dx=1, dy=0)
        if key == tcod.event.K_ESCAPE:
            return EscapeAction()

        return None
