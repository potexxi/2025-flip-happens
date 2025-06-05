import pygame
import src.submodule.globals as g
import src.submodule.level2.place_assets as assets
import src.submodule.skater.skater as player
from src.submodule.level1.place_assets import draw_clock
from src.submodule.level1.play import draw_coins_collected

coins_collected: int = 0
def play(screen: pygame.Surface) -> str:
    """
    play the level2 funktion
    :param screen: pygame.Surface -> where the level2 shall be drawn
    :return: the current game mode
    """
    player_rect = pygame.Rect((player.x_position, player.y_position, g.PLAYER_SIZE, g.PLAYER_SIZE))
    assets.draw_assets(screen, player_rect)
    player.draw(screen)
    player.move()
    assets.time = draw_clock(screen, assets.time)
    draw_coins_collected(screen, coins_collected)
    return "level2"