import pygame
import src.submodule.level1.place_blocks as draw_level
import src.submodule.skater.skater as player

last_timestamp: int = None
mode: str = "play"


def play(screen: pygame.Surface) -> str:
    """
    Play level1
    :param screen: pygame.Surface -> where the game should be drawn
    :return: str -> in which mode the game is in
    """
    global mode
    mode = draw_level.draw(screen)
    mode = player.move()
    player.draw(screen)

    return mode
