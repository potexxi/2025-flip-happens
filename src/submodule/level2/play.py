import pygame
import random
import src.submodule.level1.play as level1
import src.submodule.globals as g
import src.submodule.level2.place_assets as assets
import src.submodule.skater.skater as player
from src.submodule.rain.rain import rain
import src.submodule.level1.place_assets as asset

coins_collected: int = 0#
rain_bool: bool = False
begin: bool = True


def play(screen: pygame.Surface) -> str:
    """
    play the level2 funktion
    :param screen: pygame.Surface -> where the level2 shall be drawn
    :return: the current game mode
    """
    global rain_bool
    if begin:
        if random.random() < 0.4:
            rain_bool = True
    player_rect = pygame.Rect((player.x_position, player.y_position, g.PLAYER_SIZE, g.PLAYER_SIZE))
    assets.draw_assets(screen, player_rect)
    player.draw(screen)
    # Rain:
    if rain_bool:
        rain(screen)
    # Move the player
    player.move(rain_bool)
    # draw letters
    asset.draw_letters(screen, player_rect, assets.letters2_position)

    level1.draw_coins_collected(screen, coins_collected)
    return "level2"