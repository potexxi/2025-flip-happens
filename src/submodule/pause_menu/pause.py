import pygame
import src.submodule.globals as g
import src.submodule.level1.place_blocks as level
from src.submodule.menu.menu import draw_button, check_button_collide


screen_size: tuple[float, float] = (g.WIDTH//2, g.HEIGHT//2)
last_timestamp: int = 0


def draw(screen: pygame.Surface) -> None:
    weiter_button = [screen_size[0] / 2 - screen_size[0] / 4 / 2, screen_size[1] / 3, screen_size[0] / 4,
                     screen_size[1] / 6, g.HEIGHT // 35]
    explain_button = [screen_size[0] / 2 - screen_size[0] / 4 / 2,
                      screen_size[1] / 3 + screen_size[1] / 6 + screen_size[1] / 15,
                      screen_size[0] / 4, screen_size[1] / 6, g.HEIGHT // 35]
    stop_button = [screen_size[0] / 2 - screen_size[0] / 4 / 2,
                   screen_size[1] / 3 + 2 * (screen_size[1] / 6 + screen_size[1] / 15),
                   screen_size[0] / 4, screen_size[1] / 6, g.HEIGHT // 35]

    pygame.draw.rect(screen, (20, 20, 60, 180), (0,0,screen_size[0], screen_size[1]), border_radius=10)

    draw_button(screen, "Weiter", (weiter_button[0], weiter_button[1], weiter_button[2], weiter_button[3]),
                weiter_button[4],  (211, 211, 211))
    draw_button(screen, "Stop", (stop_button[0], stop_button[1], stop_button[2], stop_button[3]),
                stop_button[4], (211, 211, 211))
    draw_button(screen, "Steuerung", (explain_button[0], explain_button[1], explain_button[2], explain_button[3]),
                explain_button[4], (211, 211, 211))

    check_button_collide(screen, "Weiter", (weiter_button[0], weiter_button[1], weiter_button[2]
                                            , weiter_button[3]), weiter_button[4] + 5, (255, 215, 0))




def check_menu_button_pressed(screen: pygame.Surface, events: list[pygame.event.Event], pause: bool) -> bool:
    """
    Check if the user presses the menu-button
    :param screen: pygame.Surface -> where the icon should be drawn
    :param events: list of pygame events
    :return: bool -> if the button gets pressed
    """
    if not pause:
        screen.blit(level.ui_pause, (level.pause_button[0], level.pause_button[1]))
    rect = pygame.Rect(level.pause_button)

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rect.collidepoint(pygame.mouse.get_pos()):
                return True
    return False


def pause(screen: pygame.Surface, esc: bool, events: list[pygame.event.Event]) -> str:
    """
    The pause-menu in the game
    :param screen: pygame.Surface -> where the menu should be drawn
    :param esc: True -> esc gets pressed -> false esc doesn't get pressed
    :return: the mode in which the game is right now (pause, start-menu, play...)
    """
    global last_timestamp
    # Draw the menu icon in time difference, so the icon doesn't get drawn too often
    timestamp = pygame.time.get_ticks()
    if timestamp - last_timestamp > 500:
        screen.blit(level.ui_pause, (level.pause_button[0], level.pause_button[1]))
    last_timestamp = timestamp

    pause_screen: pygame.Surface = pygame.Surface((screen_size[0], screen_size[1]), pygame.SRCALPHA)
    draw(pause_screen)
    screen.blit(pause_screen, (g.WIDTH//2 - screen_size[0]//2, g.HEIGHT//2 - screen_size[1]//2))

    if esc or check_menu_button_pressed(screen, events, True):
        last_timestamp = 0
        return "play"

    return "pause"


