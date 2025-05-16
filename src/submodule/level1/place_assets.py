import pygame
import src.submodule.globals as g

coins: list[pygame.Surface] = []
coins_counter: int = 0
last_timestamp: int = None
first_block_floor: tuple[float,float] = (-30, g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2) - g.ASSETS_SIZE)
first_coin = (
    first_block_floor[0] + (g.ASSETS_SIZE - g.POWER_UPS_SIZE) / 2,
    first_block_floor[1] + (g.ASSETS_SIZE//2.5)
)



def init_assets() -> None:
    """
    Load all the assets-images and scale them
    """
    global coins
    # Coins:
    image = pygame.image.load("assets/level1/coin_strip.png").convert_alpha()
    for i in range(6):
        sub_image = image.subsurface((9 * i, 0, 9, 10))
        sub_image = pygame.transform.scale(sub_image, (g.POWER_UPS_SIZE, g.POWER_UPS_SIZE))
        coins.append(sub_image)


def draw_coins(screen: pygame.Surface) -> None:
    """
    Draw the coins
    :param screen: pygame.Surface: where the coins should be drawn
    """
    global last_timestamp, coins_counter
    # get timestamp and the image
    timestamp = pygame.time.get_ticks()
    image = coins[coins_counter]

    # blit all the image at all the destinations
    for t in range(1, 4):
        screen.blit(image, (first_coin[0] + t * g.ASSETS_SIZE,
                        first_coin[1]))
    # make the timestamp for the animation
    if last_timestamp is None or timestamp - last_timestamp > 150:
        coins_counter += 1
        if coins_counter >= 6:
            coins_counter = 0
        last_timestamp = timestamp