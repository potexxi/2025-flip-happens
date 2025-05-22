import pygame
import src.submodule.globals as g
from src.submodule.menu.menu import draw_button, check_button_collide
from src.submodule.level1.place_blocks import check_menu_button_pressed

screen_size: tuple[float, float] = (g.WIDTH//2, g.HEIGHT//2)
play: bool = False

def draw(screen: pygame.Surface) -> None:
    pygame.draw.rect(screen, "white", (0,0,screen_size[0], screen_size[1]), border_radius=10)


def pause(screen: pygame.Surface, esc: bool) -> str:
    """
    The pause-menu in the game
    :param screen: pygame.Surface -> where the menu should be drawn
    :param esc: True -> esc gets pressed -> false esc doesn't get pressed
    :return: the mode in which the game is right now (pause, start-menu, play...)
    """
    global play
    pause_screen: pygame.Surface = pygame.Surface((screen_size[0], screen_size[1]), pygame.SRCALPHA)
    draw(pause_screen)
    screen.blit(pause_screen, (g.WIDTH//2 - screen_size[0]//2, g.HEIGHT//2 - screen_size[1]//2))


    if esc:
        play = not play
    if play:
        return "play"

    play = False
    return check_menu_button_pressed(screen, True)


