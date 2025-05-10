import pygame
import src.submodule.globals as g

background: pygame.Surface = None
brick: pygame.Surface = None


def init_level1() -> None:
    global background, brick
    # Background:
    background = pygame.image.load("assets/level1/background.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))
    # Brick:
    brick = pygame.image.load("assets/level1/BrickTiles.png").convert_alpha()
    brick = brick.subsurface((0,0,16,16))
    brick = pygame.transform.scale(brick, (64,64))


def level1(screen: pygame.Surface) -> str:
    screen.blit(background, (0,0))
    screen.blit(brick, (0,0))
    return "play"
