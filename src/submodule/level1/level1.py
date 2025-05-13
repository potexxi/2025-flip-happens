from typing import Optional

import pygame
import src.submodule.globals as g

background: pygame.Surface = None
brick: pygame.Surface = None
ui_pause: pygame.Surface = None
halfpipe_left: pygame.Surface = None
halfpipe_right: pygame.Surface = None
mode: str = "play"
pause_button = [g.WIDTH - g.WIDTH / 50 -5, 5, g.WIDTH / 50, g.WIDTH / 50]
first_block_floor = ( - 30, g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2) - g.ASSETS_SIZE)



def init_level1() -> None:
    """
    Init all the pictures the level 1 needs
    """
    global background, brick, ui_pause, halfpipe_left, halfpipe_right
    # Background:
    background = pygame.image.load("assets/level1/background_unsharp.png").convert_alpha()
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


def check_menu_button_pressed(screen: pygame.Surface) -> str:
    """
    Check if the user presses the menu-button
    :param screen:
    :return: str -> which mode the game is in
    """
    screen.blit(ui_pause, (pause_button[0], pause_button[1]))
    rect = pygame.Rect(pause_button)
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    if rect.collidepoint(mouse_pos) and click:
        return "pause"
    return "play"


def place_bricks(screen: pygame.Surface) -> None:
    """
    Draw the bricks on the screen
    :param screen: pygame.Surface -> where the bricks should be drawn
    """
    # Floor: .
    for t in range(g.WIDTH // g.ASSETS_SIZE + 1):
        screen.blit(brick, (g.ASSETS_SIZE * t - 30, g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2)))
        if t == 15:
            # unterer Berg beim Boden
            for y in range(3):
                screen.blit(brick, ((g.ASSETS_SIZE * t - 30) + y*g.ASSETS_SIZE,
                                    g.HEIGHT - g.ASSETS_SIZE - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2)))
    for t in range(4):
        screen.blit(brick, (first_block_floor[0] + t*g.ASSETS_SIZE,
                            first_block_floor[1] - 2*g.ASSETS_SIZE))
    for t in range(3):
        screen.blit(brick, (first_block_floor[0] + t * g.ASSETS_SIZE + 3*g.ASSETS_SIZE,
                            first_block_floor[1] - g.ASSETS_SIZE))
    for t in range(4):
        screen.blit(brick, (first_block_floor[0] + t * g.ASSETS_SIZE + 4 * g.ASSETS_SIZE,
                            first_block_floor[1] - 5 * g.ASSETS_SIZE))
    screen.blit(brick, (first_block_floor[0] + g.ASSETS_SIZE + 4 * g.ASSETS_SIZE,
                            first_block_floor[1] - 6 * g.ASSETS_SIZE))
    for t in range(3):
        screen.blit(brick, (first_block_floor[0] + t * g.ASSETS_SIZE,
                            first_block_floor[1] - 9 * g.ASSETS_SIZE))
    for t in range(2):
        screen.blit(brick, (first_block_floor[0] + t * g.ASSETS_SIZE,
                            first_block_floor[1] - 10 * g.ASSETS_SIZE))


def place_elements(screen: pygame.Surface) -> None:
    """
    Draw the elements (ramps, coins, letters etc.) on the screen
    :param screen: pygame.Surface -> where the elements should be drawn
    """
    # Ramps:
    screen.blit(halfpipe_left, ((g.ASSETS_SIZE * 15 - 30) - g.ASSETS_SIZE,
                           g.HEIGHT - g.ASSETS_SIZE - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2)))
    screen.blit(halfpipe_right, ((g.ASSETS_SIZE * 19 - 30) - g.ASSETS_SIZE,
                           g.HEIGHT - g.ASSETS_SIZE - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2)))


def level1(screen: pygame.Surface) -> str:
    """
    level1 of the game
    :param screen: pygame.Surface -> where the level should be drawn
    :return: str -> which mode the game is in
    """
    global mode
    # Background:
    screen.blit(background, (0,0))
    # Elements:
    place_bricks(screen)
    place_elements(screen)



    # Pause-Button:
    if check_menu_button_pressed(screen) == "pause":
        return "pause"

    return "play"
