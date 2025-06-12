import pygame
import copy
import src.submodule.globals as g
import src.submodule.skater.skater as player
import src.submodule.level1.place_assets as level1


background: pygame.Surface = ...
brick: pygame.Surface = ...
first_block_floor: tuple[float,float] = (-30, g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2) - g.ASSETS_SIZE)
first_asset: tuple[float,float] = (first_block_floor[0] + (g.ASSETS_SIZE - g.POWER_UPS_SIZE) / 2,
    first_block_floor[1] + (g.ASSETS_SIZE//2.5))
first_power_up: tuple[float,float] = (first_asset[0] - g.POWER_UPS_SIZE//4, first_asset[1] - g.POWER_UPS_SIZE//2)
coins_counter: int = 0
power_counter: int = 0
last_timestamp_coins: int = None
last_timestamp_power: int = None
last_timestamp_clock: int = 0
time = 120
assets_original = [
    [0,0,0,0,0,1,1,1,1,1,1,1,4,4,0,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,1,1,1],
    [1,0,0,4,0,0,0,2,2,0,0,2,2,0,0,2,2,0,1,1,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,0,5,0,0,4,4,0,0,4,4,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,6,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,4,4,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,6,0,3,0,0,0,0,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,4,4,4,0,0,0,5,1,1,1,1,1,0,0,2,2,3,2,0,0,0,0,0],
    [1,1,2,2,2,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,4,4,4,4,0,0,0,2,0],
    [1,1,1,1,1,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,1,6,0,2,0,5,0,0,0,0,0,0,0,0,4,4,1,1,1,1],
    [0,0,0,2,2,2,0,5,1,1,1,1,4,4,4,1,0,2,2,2,0,5,1,1,0,0,1,0,0,0],
    [1,1,4,4,4,1,1,1,1,1,1,1,0,0,0,1,1,4,4,4,1,1,1,1,0,1,1,0,0,0],
]
assets = copy.deepcopy(assets_original)
assets.reverse()
append_elements = True
letters_position: list[tuple] = [
    (first_asset[0] + 2 * g.ASSETS_SIZE,first_asset[1]  - 1 * g.ASSETS_SIZE),
    (first_asset[0] + 1 * g.ASSETS_SIZE, first_asset[1] - 5 * g.ASSETS_SIZE),
    (first_asset[0] + 17 * g.ASSETS_SIZE, first_asset[1]  - g.ASSETS_SIZE),
    (first_asset[0] + 12 * g.ASSETS_SIZE, first_asset[1] - 5 * g.ASSETS_SIZE),
    (first_asset[0] + 27 * g.ASSETS_SIZE,first_asset[1] - 4 * g.ASSETS_SIZE),
    (first_asset[0] + 3 * g.ASSETS_SIZE, first_asset[1] - 10 * g.ASSETS_SIZE),
    (first_asset[0] + 20 * g.ASSETS_SIZE, first_asset[1] - 13 * g.ASSETS_SIZE),
    (first_asset[0] + 1 * g.ASSETS_SIZE, first_asset[1] - 13 * g.ASSETS_SIZE),
    (first_asset[0] + 10 * g.ASSETS_SIZE, first_asset[1] - 2 * g.ASSETS_SIZE),
]


def init_assets():
    """
    Init the assets and scale them.
    """
    global background, brick
    # Background:
    background = pygame.image.load("assets/level2/background.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))

    # Bricks:
    brick = pygame.image.load("assets/level2/brick.png").convert_alpha()
    brick = brick.subsurface((3 * 16,3 * 16,16,16))
    brick = pygame.transform.scale(brick, (g.ASSETS_SIZE, g.ASSETS_SIZE))


def draw_assets(screen: pygame.Surface, player_rect: pygame.Rect) -> None:
    """
    Draw the assets of the level2
    :param screen: pygame.Surface -> where the assets shall be drawn
    :param player_rect: pygame.Rect -> the rect of the player
    """
    global append_elements, last_timestamp_power, last_timestamp_coins, coins_counter, power_counter, time
    # blit the background
    screen.blit(background, (0,0))
    # clock
    time = level1.draw_clock(screen, time)
    # blit the assets
    timestamp = pygame.time.get_ticks()
    for y, line in enumerate(assets):
        for x, item in enumerate(line):
            x_position = first_block_floor[0] + x * g.ASSETS_SIZE
            y_position = (first_block_floor[1] + g.ASSETS_SIZE) - y * g.ASSETS_SIZE
            if item == 1:
                screen.blit(brick, (x_position, y_position))
                if append_elements:
                    player.blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 2:
                x_position = first_asset[0] + x * g.ASSETS_SIZE
                y_position = first_asset[1] - (y-1) * g.ASSETS_SIZE
                screen.blit(level1.coins[coins_counter], (x_position, y_position))
                if level1.check_for_collect(1, player_rect, x_position, y_position):
                    assets[y][x] = 0

            elif item == 3:
                x_position = first_power_up[0] + x * g.ASSETS_SIZE
                y_position = first_power_up[1] - (y-1) * g.ASSETS_SIZE
                screen.blit(level1.power_up[power_counter], (x_position, y_position))
                if level1.check_for_collect(2, player_rect, x_position, y_position):
                    assets[y][x] = 0

            if item == 4:
                screen.blit(level1.pipe, (x_position, y_position))
                if append_elements:
                    player.poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 5:
                screen.blit(level1.halfpipes[0], (x_position, y_position))
                if append_elements:
                    player.halfpipes_right.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 6:
                screen.blit(level1.halfpipes[1], (x_position, y_position))
                if append_elements:
                    player.halfpipes_left.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 7:
                screen.blit(level1.fast_ramp, (x_position, y_position))
                if append_elements:
                    player.fast_ramp.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 8:
                screen.blit(level1.high_ramps[1], (x_position, y_position))
                if append_elements:
                    player.high_ramps_right.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 9:
                screen.blit(level1.high_ramps[0], (x_position, y_position))
                if append_elements:
                    player.high_ramps_left.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

    append_elements = False

    # Doing the sprite stuff for the next pictures
    if last_timestamp_coins is None or timestamp - last_timestamp_coins > 150:
        coins_counter += 1
        if coins_counter >= 5:
            coins_counter = 0
        last_timestamp_coins = timestamp
    if last_timestamp_power is None or timestamp - last_timestamp_power > 200:
        power_counter += 1
        if power_counter >= 4:
            power_counter = 0
        last_timestamp_power = timestamp

