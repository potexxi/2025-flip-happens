import pygame
import src.submodule.globals as g
from src.submodule.menu import draw_button, check_button_collide

background: pygame.Surface = None
brick: pygame.Surface = None
ui_pause: pygame.Surface = None
halfpipe: pygame.Surface = None
mode: str = "play"
pause_button = [g.WIDTH - g.WIDTH / 50 -5, 5, g.WIDTH / 50, g.WIDTH / 50]



def init_level1() -> None:
    """
    Init all the pictures the level 1 needs
    """
    global background, brick, ui_pause, halfpipe
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
    halfpipe = pygame.image.load("assets/level1/halfpipe.png")
    halfpipe = pygame.transform.scale(halfpipe, (g.ASSETS_SIZE, g.ASSETS_SIZE))


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
    # Floor:
    for t in range(g.WIDTH // g.ASSETS_SIZE + 1):
        screen.blit(brick, (g.ASSETS_SIZE * t - 30, g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2)))
        if t == 15:
            for y in range(4):
                screen.blit(brick, ((g.ASSETS_SIZE * t - 30) + y*g.ASSETS_SIZE,
                                    g.HEIGHT - g.ASSETS_SIZE - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2)))


def place_elements(screen: pygame.Surface) -> None:
    # Ramps:
    screen.blit(halfpipe, ((g.ASSETS_SIZE * 15 - 30) - g.ASSETS_SIZE,
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
    # Pause - button
    mode = check_menu_button_pressed(screen)
    return mode