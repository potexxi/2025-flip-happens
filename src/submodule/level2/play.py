import pygame
import src.submodule.level2.place_assets as assets
import src.submodule.skater.skater as player


def play(screen: pygame.Surface) -> str:
    assets.draw_assets(screen)
    player.draw(screen)
    player.move()
    return "level2"