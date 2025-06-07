import pygame
import src.submodule.globals as g
import src.submodule.menu.menu as menu


def draw(screen: pygame.Surface) -> None:
    # Background:
    menu.move_background("start")
    background = pygame.image.load("assets/menu/blue_unsharp.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))
    screen.blit(background, g.POSITION_WORLD)
    screen.blit(background, (g.POSITION_WORLD[0] + screen.get_width(), g.POSITION_WORLD[1]))

    #


def shop(screen: pygame.Surface) -> str:
    draw(screen)
    return "shop"