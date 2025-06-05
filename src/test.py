import pygame
from src.submodule.level1.place_assets import init_assets
import src.submodule.globals as g

drops = []
drop_counter = 0
last_timestamp_drop = 0

def init():
    # big = pygame.image.load(f"assets/rain/rain1.png").convert_alpha()
    # for number in range(10):
    #     drop = big.subsurface((number * 64, 0, 64,64))
    #     drop = pygame.transform.scale(drop, (300,300))
    #     drops.append(drop)
    big = pygame.image.load(f"assets/rain/rain.png").convert_alpha()
    for number in range(16):
        drop = big.subsurface((number * 64, 0, 64,64))
        drop = pygame.transform.scale(drop, (g.WIDTH/(g.WIDTH/150),g.HEIGHT/(g.HEIGHT/150)))
        drops.append(drop)

def rain(screen: pygame.Surface) -> None:
    global drop_counter, last_timestamp_drop
    line = int(g.WIDTH//(g.WIDTH/(g.WIDTH/150)))
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

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("test")
    screen = pygame.display.set_mode((0,0))
    clock = pygame.time.Clock()

    init_assets()
    init()

    from src.submodule.level1.place_assets import background
    while True:
        screen.blit(background, (0,0))
        rain(screen)



        pygame.display.flip()

        clock.tick(g.FPS)