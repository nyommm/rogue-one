import tcod
from lib import Engine, Entity, EventHandler

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

WHITE_COLOR = (255, 255, 255)


def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        './assets/dejavu10x10_gs_tc.png', 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    player = Entity(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, '@', WHITE_COLOR)
    engine = Engine({player}, EventHandler(), player)
    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        tileset=tileset,
        title='rogue-one',
        vsync=True
    ) as context:
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order='F')
        while True:
            engine.render(root_console, context)
            engine.handle_events(tcod.event.wait())


if __name__ == '__main__':
    main()
