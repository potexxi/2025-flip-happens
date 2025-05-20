import pygame
import src.submodule.level1.draw as draw_level
import src.submodule.skater.skin as player

last_timestamp: int = None
mode: str = "play"


def play(screen: pygame.Surface) -> str:
    """
    Play level1
    :param screen: pygame.Surface -> where the game should be drawn
    :return: str -> in which mode the game is
    """
    global last_timestamp, mode
    mode = draw_level.draw(screen)
    print(mode)
    timestamp = pygame.time.get_ticks()
    player_mode = "drive"
    if last_timestamp is None or timestamp - last_timestamp > 500:
        player_mode = "drive"
        last_timestamp = timestamp
    player.draw(screen, player_mode)


    return mode
