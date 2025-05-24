import pygame
import src.submodule.globals as g

background: pygame.Surface = ...
brick: pygame.Surface = ...
ui_pause: pygame.Surface = ...
halfpipe_left: pygame.Surface = ...
halfpipe_right: pygame.Surface = ...
pipe: pygame.Surface = ...
wide_ramp: pygame.Surface = ...
high_ramp_left: pygame.Surface = ...
high_ramp_right: pygame.Surface = ...
mode: str = "play"
pause_button: tuple[float,float,float,float] = (g.WIDTH - g.WIDTH / 50 -5, 5, g.WIDTH / 50, g.WIDTH / 50)
first_block_floor: tuple[float,float] = (-30, g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2) - g.ASSETS_SIZE)
blocks: list[tuple] = []
poles: list[tuple] = []
fast_ramp: list[tuple] = []
halfpipes_right: list[tuple] = []
halfpipes_left: list[tuple] = []
append_blocks: bool = True
append_poles: bool = True
append_ramps: bool = True


def init_blocks() -> None:
    """
    Init all the pictures the level 1 needs
    """
    global background, brick, ui_pause, halfpipe_left, halfpipe_right, pipe, high_ramp_left, wide_ramp, high_ramp_right
    # Background:
    background = pygame.image.load("assets/level1/background.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))

    # Brick:
    brick = pygame.image.load("assets/level1/BrickTiles.png").convert_alpha()
    brick = brick.subsurface((0,0,16,16))
    brick = pygame.transform.scale(brick, (g.ASSETS_SIZE,g.ASSETS_SIZE))

    # Pause Button:
    ui_pause = pygame.image.load("assets/ui-controls/menu.png").convert_alpha()
    ui_pause = pygame.transform.scale(ui_pause, (pause_button[2],pause_button[3]))

    # Halfpipe:
    halfpipe_left = pygame.image.load("assets/level1/halfpipe.png")
    halfpipe_left = pygame.transform.scale(halfpipe_left, (g.ASSETS_SIZE, g.ASSETS_SIZE))
    halfpipe_right = pygame.transform.flip(halfpipe_left, True,False)

    # Pipe:
    pipe = pygame.image.load("assets/level1/pipe.png").convert_alpha()
    pipe = pygame.transform.scale(pipe, (g.ASSETS_SIZE, g.ASSETS_SIZE))

    # Ramps:
    high_ramp_left = pygame.image.load("assets/level1/high_ramp_left.png").convert_alpha()
    high_ramp_left = pygame.transform.scale(high_ramp_left, (g.ASSETS_SIZE, g.ASSETS_SIZE))
    high_ramp_right = pygame.image.load("assets/level1/high_ramp_right.png").convert_alpha()
    high_ramp_right = pygame.transform.scale(high_ramp_right, (g.ASSETS_SIZE, g.ASSETS_SIZE))
    wide_ramp = pygame.image.load("assets/level1/wide_ramp.png").convert_alpha()
    wide_ramp = pygame.transform.scale(wide_ramp, (g.ASSETS_SIZE, g.ASSETS_SIZE))


def place_bricks(screen: pygame.Surface) -> None:
    """
    Draw the bricks on the screen
    :param screen: pygame.Surface -> where the bricks should be drawn
    """
    global append_blocks
    for t in range(g.WIDTH // g.ASSETS_SIZE + 1):
        x = g.ASSETS_SIZE * t - 30
        y = g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2)
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))
        if t == 9:
            for z in range(3):
                x2 = x + z * g.ASSETS_SIZE
                y2 = g.HEIGHT - g.ASSETS_SIZE - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2)
                screen.blit(brick, (x2, y2))
                if append_blocks:
                    blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x2, y2))

    for t in range(5):
        x = first_block_floor[0] + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 4 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(10):
        x = first_block_floor[0] + 8 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 4 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] + 18 * g.ASSETS_SIZE
        y = first_block_floor[1] - 4 * g.ASSETS_SIZE - t * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] + 19 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 6 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(4):
        x = first_block_floor[0] + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 8 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(2):
        x = first_block_floor[0] + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 9 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] + t * g.ASSETS_SIZE + 9 * g.ASSETS_SIZE
        y = first_block_floor[1] - g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(2):
        x = first_block_floor[0] + 27 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 4 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(2):
        x = first_block_floor[0] + 9 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 8 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(2):
        x = first_block_floor[0] + 8 * g.ASSETS_SIZE
        y = first_block_floor[1] - 9 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(2):
        x = first_block_floor[0] + 7 * g.ASSETS_SIZE
        y = first_block_floor[1] - 10 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] - 1 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 12 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] + 11 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 8 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] + 13 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 7 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(8):
        x = first_block_floor[0] + 21 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 9 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(2):
        for z in range(6):
            x = first_block_floor[0] + 23 * g.ASSETS_SIZE + z * g.ASSETS_SIZE
            y = first_block_floor[1] - 10 * g.ASSETS_SIZE - t * g.ASSETS_SIZE
            screen.blit(brick, (x, y))
            if append_blocks:
                blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(5):
        x = first_block_floor[0] + 24 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 12 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] + 7 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 13 * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(2):
        x = first_block_floor[0] + 7 * g.ASSETS_SIZE
        y = first_block_floor[1] - 14 * g.ASSETS_SIZE - t * g.ASSETS_SIZE
        screen.blit(brick, (x, y))
        if append_blocks:
            blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))
    append_blocks = False


def place_elements(screen: pygame.Surface) -> None:
    """
    Draw the elements (ramps, coins, letters etc.) on the screen
    :param screen: pygame.Surface -> where the elements should be drawn
    """
    global append_poles
    # Halfpipes:
    x = first_block_floor[0] + 12 * g.ASSETS_SIZE
    y = first_block_floor[1]
    screen.blit(halfpipe_right, (x,y))
    if append_ramps:
        halfpipes_right.append((x, y))

    x = first_block_floor[0] + 2 * g.ASSETS_SIZE
    y = first_block_floor[1] - 9 * g.ASSETS_SIZE
    screen.blit(halfpipe_right, (x, y))
    if append_ramps:
        halfpipes_right.append((x, y))

    x = first_block_floor[0] + 9 * g.ASSETS_SIZE
    y = first_block_floor[1] - 9 * g.ASSETS_SIZE
    screen.blit(halfpipe_right, (x, y))
    if append_ramps:
        halfpipes_right.append((x, y))

    x = first_block_floor[0] + 4 * g.ASSETS_SIZE
    y = first_block_floor[1] - 5 * g.ASSETS_SIZE
    screen.blit(halfpipe_left, (x, y))
    if append_ramps:
        halfpipes_left.append((x, y))

    x = first_block_floor[0] + 22 * g.ASSETS_SIZE
    y = first_block_floor[1] - 10 * g.ASSETS_SIZE
    screen.blit(halfpipe_left, (x, y))
    if append_ramps:
        halfpipes_left.append((x, y))

    x = first_block_floor[0] + 8 * g.ASSETS_SIZE
    y = first_block_floor[1]
    screen.blit(halfpipe_left, (x,y))
    if append_ramps:
        halfpipes_left.append((x, y))

    x = first_block_floor[0] + 17 * g.ASSETS_SIZE
    y = first_block_floor[1] - 5 * g.ASSETS_SIZE
    screen.blit(halfpipe_left, (x, y))
    if append_ramps:
        halfpipes_left.append((x, y))

    # Pipes:
    for t in range(3):
        x = first_block_floor[0] + 5 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 4 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(6):
        x = first_block_floor[0] + t*g.ASSETS_SIZE
        y = first_block_floor[1] - g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(6):
        x = first_block_floor[0] + 14 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(4):
        x = first_block_floor[0] + 20 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 2 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] + 24 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 3 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] + 23 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 5 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(2):
        x = first_block_floor[0] + 5 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 10 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] + 2 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 11 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(2):
        x = first_block_floor[0] + 6 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 6 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(3):
        x = first_block_floor[0] + 18 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 8 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(2):
        x = first_block_floor[0] + 15 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 9 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(6):
        x = first_block_floor[0] + 15 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 12 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    for t in range(4):
        x = first_block_floor[0] + 10 * g.ASSETS_SIZE + t * g.ASSETS_SIZE
        y = first_block_floor[1] - 13 * g.ASSETS_SIZE
        screen.blit(pipe, (x,y))
        if append_poles:
            poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))

    x = first_block_floor[0] + 4 * g.ASSETS_SIZE
    y = first_block_floor[1] - 7 * g.ASSETS_SIZE
    screen.blit(pipe, (x,y))
    if append_poles:
        poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x, y))
    append_poles = False

    # # Ramps:
    # fast ramps (ramps goes up and down, you get faster for a moment)
    x = first_block_floor[0] + 11 * g.ASSETS_SIZE
    y = first_block_floor[1] - 5 * g.ASSETS_SIZE
    screen.blit(wide_ramp, (x,y))
    if append_ramps:
        fast_ramp.append((g.ASSETS_SIZE,g.ASSETS_SIZE,x,y))

    x = first_block_floor[0] + 11 * g.ASSETS_SIZE
    y = first_block_floor[1] - 9 * g.ASSETS_SIZE
    screen.blit(wide_ramp, (x,y))
    if append_ramps:
        fast_ramp.append((g.ASSETS_SIZE,g.ASSETS_SIZE,x,y))

    x = first_block_floor[0] + 24 * g.ASSETS_SIZE
    y = first_block_floor[1] - 13 * g.ASSETS_SIZE
    screen.blit(high_ramp_right, (x,y))
    if append_ramps:
        fast_ramp.append((g.ASSETS_SIZE,g.ASSETS_SIZE,x,y))

    # high ramps (you jump in the front)
    x = first_block_floor[0] + 11 * g.ASSETS_SIZE
    y = first_block_floor[1] - 2 * g.ASSETS_SIZE
    screen.blit(high_ramp_left, (x,y))

    x = first_block_floor[0] + 9 * g.ASSETS_SIZE
    y = first_block_floor[1] - 2 * g.ASSETS_SIZE
    screen.blit(high_ramp_right, (x, y))
