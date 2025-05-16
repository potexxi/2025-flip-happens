import pygame
import src.submodule.globals as g

coins: list[pygame.Surface] = []
letters: list[pygame.Surface] = []
power_up: list[pygame.Surface] = []
coins_counter: int = 0
power_counter: int = 0
last_timestamp: int = None
last_timestamp_power: int = None
first_block_floor: tuple[float,float] = (-30, g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2) - g.ASSETS_SIZE)
first_asset: tuple[float,float] = (first_block_floor[0] + (g.ASSETS_SIZE - g.POWER_UPS_SIZE) / 2,
    first_block_floor[1] + (g.ASSETS_SIZE//2.5))
first_power_up: tuple[float,float] = (first_asset[0] - g.POWER_UPS_SIZE//4, first_asset[1] - g.POWER_UPS_SIZE//2)



def init_assets() -> None:
    """
    Load all the assets-images and scale them
    """
    global coins, letters, power_up
    # Coins:
    image = pygame.image.load("assets/level1/coin_sprite.png").convert_alpha()
    for i in range(5):
        sub_image = image.subsurface((16 * i, 0, 16, 16))
        sub_image = pygame.transform.scale(sub_image, (g.POWER_UPS_SIZE, g.POWER_UPS_SIZE))
        coins.append(sub_image)
    # Letters:
    image = pygame.image.load("assets/level1/letters.png").convert_alpha()
    for i in range(9):
        sub_image = image.subsurface((16 * i + 3 + i, 0, 16, 28))
        sub_image = pygame.transform.scale(sub_image, (g.POWER_UPS_SIZE, g.POWER_UPS_SIZE +g.POWER_UPS_SIZE // 4))
        letters.append(sub_image)
    # Power-Up:
    image = pygame.image.load("assets/level1/power_up_sprite.png").convert_alpha()
    for i in range(4):
        sub_image = image.subsurface((16 * i, 0, 16, 16))
        sub_image = pygame.transform.scale(sub_image, (g.POWER_UPS_SIZE + g.POWER_UPS_SIZE//2,
                                                       g.POWER_UPS_SIZE+ g.POWER_UPS_SIZE//2))
        power_up.append(sub_image)


def draw_coins(screen: pygame.Surface) -> None:
    """
    Draw the coins
    :param screen: pygame.Surface: where the coins should be drawn
    """
    global last_timestamp, coins_counter
    # get timestamp and the image
    timestamp = pygame.time.get_ticks()
    image = coins[coins_counter]

    # blit all the coin - images at all the destinations
    for t in range(1, 5):
        screen.blit(image, (first_asset[0] + t * g.ASSETS_SIZE,
                        first_asset[1]))
    for t in range(1, 4):
        screen.blit(image, (first_asset[0] + t * g.ASSETS_SIZE + 15 * g.ASSETS_SIZE,
                        first_asset[1]))
    for t in range(1, 4):
        screen.blit(image, (first_asset[0] + t * g.ASSETS_SIZE + 19 * g.ASSETS_SIZE,
                        first_asset[1]))
    for t in range(3):
        screen.blit(image, (first_asset[0] + t * g.ASSETS_SIZE + 3 * g.ASSETS_SIZE,
                            first_asset[1] - 2 * g.ASSETS_SIZE))
    for t in range(3):
        screen.blit(image, (first_asset[0] + t * g.ASSETS_SIZE + 2 * g.ASSETS_SIZE,
                            first_asset[1] - 12 * g.ASSETS_SIZE))
    screen.blit(image, (first_asset[0] + 13 * g.ASSETS_SIZE,
                        first_asset[1] - 5 * g.ASSETS_SIZE))
    screen.blit(image, (first_asset[0] + 15 * g.ASSETS_SIZE,
                        first_asset[1] - 5 * g.ASSETS_SIZE))
    for t in range(2):
        screen.blit(image, (first_asset[0] + 8 * g.ASSETS_SIZE + t * g.ASSETS_SIZE,
                            first_asset[1] - 5 * g.ASSETS_SIZE))
    for t in range(2):
        screen.blit(image, (first_asset[0] + 2 * g.ASSETS_SIZE + t * g.ASSETS_SIZE,
                        first_asset[1] - 5 * g.ASSETS_SIZE))
    screen.blit(image, (first_asset[0] + 3 * g.ASSETS_SIZE,
                        first_asset[1] - 9 * g.ASSETS_SIZE))
    for t in range(3):
        screen.blit(image, (first_asset[0] + 18 * g.ASSETS_SIZE + t * g.ASSETS_SIZE,
                            first_asset[1] - 9 * g.ASSETS_SIZE))
    for t in range(1, 4):
        screen.blit(image, (first_asset[0] + t * g.ASSETS_SIZE + 13 * g.ASSETS_SIZE,
                        first_asset[1] - 2 * g.ASSETS_SIZE))
    for t in range(1, 4):
        screen.blit(image, (first_asset[0] + t * g.ASSETS_SIZE + 15 * g.ASSETS_SIZE,
                        first_asset[1] - 13 * g.ASSETS_SIZE))
    for t in range(3):
        screen.blit(image, (first_asset[0] + 23 * g.ASSETS_SIZE + t * g.ASSETS_SIZE,
                        first_asset[1] - 6 * g.ASSETS_SIZE))
    screen.blit(image, (first_asset[0] + 27 * g.ASSETS_SIZE,
                        first_asset[1] - 5 * g.ASSETS_SIZE))
    screen.blit(image, (first_asset[0] + 26 * g.ASSETS_SIZE,
                        first_asset[1] - 13 * g.ASSETS_SIZE))#
    for t in range(2):
        screen.blit(image, (first_asset[0] + 12 * g.ASSETS_SIZE + t * g.ASSETS_SIZE,
                            first_asset[1] - 9 * g.ASSETS_SIZE))
    # make the timestamp for the animation
    if last_timestamp is None or timestamp - last_timestamp > 150:
        coins_counter += 1
        if coins_counter >= 5:
            coins_counter = 0
        last_timestamp = timestamp


def draw_letters(screen: pygame.Surface) -> None:
    """
    Draw the letters
    :param screen: pygame.Surface: where the letters should be drawn
    """
    screen.blit(letters[0], (first_asset[0] + g.ASSETS_SIZE
                             ,first_asset[1] - 2 *  g.ASSETS_SIZE))
    screen.blit(letters[1], (first_asset[0] + 20 *  g.ASSETS_SIZE
                                 , first_asset[1] - 7 * g.ASSETS_SIZE))
    screen.blit(letters[2], (first_asset[0] + g.ASSETS_SIZE
                                 , first_asset[1] - 13 * g.ASSETS_SIZE))
    screen.blit(letters[3], (first_asset[0] + 27 * g.ASSETS_SIZE
                                 , first_asset[1] -  13 * g.ASSETS_SIZE))
    screen.blit(letters[4], (first_asset[0] + 8 * g.ASSETS_SIZE
                                 , first_asset[1] - 14 * g.ASSETS_SIZE))
    screen.blit(letters[5], (first_asset[0] + 26 * g.ASSETS_SIZE
                                 , first_asset[1]))
    screen.blit(letters[6], (first_asset[0] + 1 * g.ASSETS_SIZE
                                 , first_asset[1] - 5 * g.ASSETS_SIZE))
    screen.blit(letters[7], (first_asset[0] + g.ASSETS_SIZE
                                 , first_asset[1] - 10 * g.ASSETS_SIZE))
    screen.blit(letters[8], (first_asset[0] + 10 * g.ASSETS_SIZE
                                 , first_asset[1] - 2 * g.ASSETS_SIZE))


def draw_power_ups(screen: pygame.Surface) -> None:
    #screen.blit(power_up, (first_asset[0] + 3 * g.ASSETS_SIZE,
                          # first_asset[1] - 10 * g.ASSETS_SIZE))
    global last_timestamp_power, power_counter
    # get timestamp and the image
    timestamp = pygame.time.get_ticks()
    image = power_up[power_counter]

    # blit all the coin - images at all the destinations
    screen.blit(image, (first_power_up[0] + 19 * g.ASSETS_SIZE,
                            first_power_up[1]))
    screen.blit(image, (first_power_up[0] + 14 * g.ASSETS_SIZE,
                            first_power_up[1] - 5 * g.ASSETS_SIZE))
    screen.blit(image, (first_power_up[0] + 11 * g.ASSETS_SIZE,
                        first_power_up[1] - 14 * g.ASSETS_SIZE))
    # make the timestamp for the animation
    if last_timestamp_power is None or timestamp - last_timestamp_power > 200:
        power_counter += 1
        if power_counter >= 4:
            power_counter = 0
        last_timestamp_power = timestamp