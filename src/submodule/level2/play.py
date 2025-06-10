import pygame
import random
import src.submodule.level1.play as level1
import src.submodule.globals as g
import src.submodule.level2.place_assets as assets2
import src.submodule.skater.skater as player
from src.submodule.rain.rain import rain
import src.submodule.level1.place_assets as assets1

coins_collected: int = 0
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
            rain_bool = False
    player_rect = pygame.Rect((player.x_position, player.y_position, g.PLAYER_SIZE, g.PLAYER_SIZE))
    assets2.draw_assets(screen, player_rect)
    # Move the player
    player.move(rain_bool)
    # draw letters
    pygame.draw.rect(screen, (59, 59, 59), (-10, -10, g.WIDTH // 8.5, g.HEIGHT // 15), border_radius=5)
    assets1.draw_letters(screen, player_rect, assets2.letters_position)
    level1.draw_letter_percentage(screen)
    # Player:
    player.draw(screen)
    # Rain:
    if rain_bool:
        rain(screen)
    level1.check_for_win_lose(screen, assets2.time)

    level1.draw_coins_collected(screen, coins_collected)
    return "level2"