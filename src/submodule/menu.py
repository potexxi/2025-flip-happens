import pygame
import src.submodule.globals as g

background: pygame.Surface = None


def init_background():
    global background
    background = pygame.image.load("assets/menu-background/10.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))


def menu(screen: pygame.Surface) -> None:
    screen.fill("white")
    screen.blit(background, (0,0))
    return None