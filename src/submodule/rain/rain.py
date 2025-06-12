import pygame
import submodule.globals as g

drops = []
drop_counter = 0
last_timestamp_drop = 0


def init() -> None:
    """
    Init the pictures of the rain-sprite
    """
    big = pygame.image.load(f"assets/rain/rain.png").convert_alpha()
    for number in range(16):
        drop = big.subsurface((number * 64, 0, 64,64))
        drop = pygame.transform.scale(drop, (g.WIDTH/(g.WIDTH/150),g.HEIGHT/(g.HEIGHT/150)))
        drops.append(drop)


def rain(screen: pygame.Surface) -> None:
    """
    Blit the rain-animation on the screen
    :param screen: pygame.Surface -> where the rain shall be drawn
    """
    global drop_counter, last_timestamp_drop
    line = int(g.WIDTH//(g.WIDTH/(g.WIDTH/150))) + 3
    height = int(g.HEIGHT//(g.HEIGHT/(g.HEIGHT/150)))
    for x in range(height + 1):
        for t in range(line):
            screen.blit(drops[drop_counter], (t*150,x*150))

    timestamp = pygame.time.get_ticks()
    if timestamp - last_timestamp_drop > 40:
        drop_counter += 1
        if drop_counter >= 16:
            drop_counter = 0
        last_timestamp_drop = timestamp