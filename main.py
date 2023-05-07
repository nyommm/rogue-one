import tcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

def main() -> None:
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    tileset = tcod.tileset.load_tilesheet(
        './assets/dejavu10x10_gs_tc.png', 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        tileset=tileset,
        title='rogue-one',
        vsync=True
    ) as context:
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order='F')
        while True:
            root_console.print(x=player_x, y=player_y, string='@')
            context.present(root_console)
            for event in tcod.event.wait():
                if event.type == 'QUIT': raise SystemExit()


if __name__ == '__main__':
    main()
