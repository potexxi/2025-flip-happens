import pygame
import copy
import src.submodule.globals as g
import src.submodule.skater.skater as player

background: pygame.Surface = ...
brick: pygame.Surface = ...
first_block_floor: tuple[float,float] = (-30, g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2) - g.ASSETS_SIZE)
first_asset: tuple[float,float] = (first_block_floor[0] + (g.ASSETS_SIZE - g.POWER_UPS_SIZE) / 2,
    first_block_floor[1] + (g.ASSETS_SIZE//2.5))
first_power_up: tuple[float,float] = (first_asset[0] - g.POWER_UPS_SIZE//4, first_asset[1] - g.POWER_UPS_SIZE//2)
assets_original = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
assets = copy.deepcopy(assets_original)
assets.reverse()
append_elements = True

def init_assets():
    global background, brick
    # Background:
    background = pygame.image.load("assets/level2/background.png")
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))

    # Bricks:
    brick = pygame.image.load("assets/level2/brick.png").convert_alpha()
    brick = brick.subsurface((3 * 16,3 * 16,16,16))
    brick = pygame.transform.scale(brick, (g.ASSETS_SIZE, g.ASSETS_SIZE))


def draw_assets(screen: pygame.Surface) -> None:
    global append_elements
    # blit the background
    screen.blit(background, (0,0))
    timestamp = pygame.time.get_ticks()
    for y, line in enumerate(assets):
        for x, item in enumerate(line):
            x_position = first_block_floor[0] + x * g.ASSETS_SIZE
            y_position = (first_block_floor[1] + g.ASSETS_SIZE) - y * g.ASSETS_SIZE
            if item == 1:
                screen.blit(brick, (x_position, y_position))
                if append_elements:
                    player.blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))
    append_elements = False
