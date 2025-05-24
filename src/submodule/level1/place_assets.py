import pygame
import src.submodule.globals as g

coins: list[pygame.Surface] = []
letters: list[pygame.Surface] = []
power_up: list[pygame.Surface] = []
coins_counter: int = 0
power_counter: int = 0
last_timestamp_coins: int = None
last_timestamp_power: int = None
last_timestamp_clock: int = 0
time: int = 120
first_block_floor: tuple[float,float] = (-30, g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2) - g.ASSETS_SIZE)
first_asset: tuple[float,float] = (first_block_floor[0] + (g.ASSETS_SIZE - g.POWER_UPS_SIZE) / 2,
    first_block_floor[1] + (g.ASSETS_SIZE//2.5))
first_power_up: tuple[float,float] = (first_asset[0] - g.POWER_UPS_SIZE//4, first_asset[1] - g.POWER_UPS_SIZE//2)

coins_position_original: list[tuple] = [
    (first_asset[0] + 1 * g.ASSETS_SIZE,first_asset[1]), (first_asset[0] + 2 * g.ASSETS_SIZE,first_asset[1]),
    (first_asset[0] + 3 * g.ASSETS_SIZE, first_asset[1]), (first_asset[0] + 4 * g.ASSETS_SIZE, first_asset[1]),
    (first_asset[0] + 1 * g.ASSETS_SIZE + 15 * g.ASSETS_SIZE, first_asset[1]), (first_asset[0] + 2 * g.ASSETS_SIZE + 15 * g.ASSETS_SIZE, first_asset[1]),
    (first_asset[0] + 3 * g.ASSETS_SIZE + 15 * g.ASSETS_SIZE, first_asset[1]), (first_asset[0] + 4 * g.ASSETS_SIZE + 15 * g.ASSETS_SIZE, first_asset[1]),
    (first_asset[0] + 1 * g.ASSETS_SIZE + 19 * g.ASSETS_SIZE, first_asset[1]), (first_asset[0] + 2 * g.ASSETS_SIZE + 19 * g.ASSETS_SIZE, first_asset[1]),
    (first_asset[0] + 3 * g.ASSETS_SIZE + 19 * g.ASSETS_SIZE, first_asset[1]), (first_asset[0] + 4 * g.ASSETS_SIZE + 19 * g.ASSETS_SIZE, first_asset[1]),
    (first_asset[0] + 0 * g.ASSETS_SIZE + 3 * g.ASSETS_SIZE, first_asset[1] - 2 * g.ASSETS_SIZE),
    (first_asset[0] + 1 * g.ASSETS_SIZE + 3 * g.ASSETS_SIZE, first_asset[1] - 2 * g.ASSETS_SIZE),
    (first_asset[0] + 2 * g.ASSETS_SIZE + 3 * g.ASSETS_SIZE, first_asset[1] - 2 * g.ASSETS_SIZE),
    (first_asset[0] + 0 * g.ASSETS_SIZE + 2 * g.ASSETS_SIZE, first_asset[1] - 12 * g.ASSETS_SIZE),
    (first_asset[0] + 1 * g.ASSETS_SIZE + 2 * g.ASSETS_SIZE, first_asset[1] - 12 * g.ASSETS_SIZE),
    (first_asset[0] + 2 * g.ASSETS_SIZE + 2 * g.ASSETS_SIZE, first_asset[1] - 12 * g.ASSETS_SIZE),
    (first_asset[0] + 13 * g.ASSETS_SIZE, first_asset[1] - 5 * g.ASSETS_SIZE),
    (first_asset[0] + 15 * g.ASSETS_SIZE, first_asset[1] - 5 * g.ASSETS_SIZE),
    (first_asset[0] + 8 * g.ASSETS_SIZE + 0 * g.ASSETS_SIZE, first_asset[1] - 5 * g.ASSETS_SIZE),
    (first_asset[0] + 8 * g.ASSETS_SIZE + 1 * g.ASSETS_SIZE, first_asset[1] - 5 * g.ASSETS_SIZE),
    (first_asset[0] + 2 * g.ASSETS_SIZE + 0 * g.ASSETS_SIZE, first_asset[1] - 5 * g.ASSETS_SIZE),
    (first_asset[0] + 2 * g.ASSETS_SIZE + 1 * g.ASSETS_SIZE, first_asset[1] - 5 * g.ASSETS_SIZE),
    (first_asset[0] + 3 * g.ASSETS_SIZE, first_asset[1] - 9 * g.ASSETS_SIZE),
    (first_asset[0] + 18 * g.ASSETS_SIZE + 0 * g.ASSETS_SIZE, first_asset[1] - 9 * g.ASSETS_SIZE),
    (first_asset[0] + 18 * g.ASSETS_SIZE + 1 * g.ASSETS_SIZE, first_asset[1] - 9 * g.ASSETS_SIZE),
    (first_asset[0] + 18 * g.ASSETS_SIZE + 2 * g.ASSETS_SIZE, first_asset[1] - 9 * g.ASSETS_SIZE),
    (first_asset[0] + 1 * g.ASSETS_SIZE + 13 * g.ASSETS_SIZE, first_asset[1] - 2 * g.ASSETS_SIZE),
    (first_asset[0] + 2 * g.ASSETS_SIZE + 13 * g.ASSETS_SIZE, first_asset[1] - 2 * g.ASSETS_SIZE),
    (first_asset[0] + 3 * g.ASSETS_SIZE + 13 * g.ASSETS_SIZE, first_asset[1] - 2 * g.ASSETS_SIZE),
    (first_asset[0] + 1 * g.ASSETS_SIZE + 15 * g.ASSETS_SIZE, first_asset[1] - 13 * g.ASSETS_SIZE),
    (first_asset[0] + 2 * g.ASSETS_SIZE + 15 * g.ASSETS_SIZE, first_asset[1] - 13 * g.ASSETS_SIZE),
    (first_asset[0] + 3 * g.ASSETS_SIZE + 15 * g.ASSETS_SIZE, first_asset[1] - 13 * g.ASSETS_SIZE),
    (first_asset[0] + 23 * g.ASSETS_SIZE + 0 * g.ASSETS_SIZE, first_asset[1] - 6 * g.ASSETS_SIZE),
    (first_asset[0] + 23 * g.ASSETS_SIZE + 1 * g.ASSETS_SIZE, first_asset[1] - 6 * g.ASSETS_SIZE),
    (first_asset[0] + 23 * g.ASSETS_SIZE + 2 * g.ASSETS_SIZE, first_asset[1] - 6 * g.ASSETS_SIZE),
    (first_asset[0] + 27 * g.ASSETS_SIZE, first_asset[1] - 5 * g.ASSETS_SIZE),
    (first_asset[0] + 26 * g.ASSETS_SIZE, first_asset[1] - 13 * g.ASSETS_SIZE),
    (first_asset[0] + 12 * g.ASSETS_SIZE + 0 * g.ASSETS_SIZE, first_asset[1] - 9 * g.ASSETS_SIZE),
    (first_asset[0] + 12 * g.ASSETS_SIZE + 1 * g.ASSETS_SIZE, first_asset[1] - 9 * g.ASSETS_SIZE)
]
coins_position: list[tuple] = coins_position_original.copy()
coins_remove: list[tuple] = []

letters_position: list[tuple] = [
    (first_asset[0] + g.ASSETS_SIZE,first_asset[1] - 2 *  g.ASSETS_SIZE),
    (first_asset[0] + 20 *  g.ASSETS_SIZE, first_asset[1] - 7 * g.ASSETS_SIZE),
    (first_asset[0] + g.ASSETS_SIZE, first_asset[1] - 13 * g.ASSETS_SIZE),
    (first_asset[0] + 27 * g.ASSETS_SIZE, first_asset[1] -  13 * g.ASSETS_SIZE),
    (first_asset[0] + 8 * g.ASSETS_SIZE, first_asset[1] - 14 * g.ASSETS_SIZE),
    (first_asset[0] + 26 * g.ASSETS_SIZE, first_asset[1]),
    (first_asset[0] + 1 * g.ASSETS_SIZE, first_asset[1] - 5 * g.ASSETS_SIZE),
    (first_asset[0] + g.ASSETS_SIZE, first_asset[1] - 10 * g.ASSETS_SIZE),
    (first_asset[0] + 10 * g.ASSETS_SIZE, first_asset[1] - 2 * g.ASSETS_SIZE)
]
next_letter_idx: int = 0

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


def draw_coins(screen: pygame.Surface, player_rect: pygame.Rect) -> None:
    """
    Draw the coins
    :param screen: pygame.Surface: where the coins should be drawn
    :param player_rect: pygame.Rect -> the rect of the player
    """
    global last_timestamp_coins, coins_counter
    # get timestamp and the image
    timestamp = pygame.time.get_ticks()
    image = coins[coins_counter]

    # remove the coins, that are collected
    for coin in coins_remove:
        coins_position.remove(coin)
    coins_remove.clear()

    # blit the coins at their destinations
    for coin in coins_position:
        screen.blit(image, coin)
        coin_rect = pygame.Rect((coin[0], coin[1], g.POWER_UPS_SIZE, g.POWER_UPS_SIZE))

        if player_rect.colliderect(coin_rect):
            coins_remove.append(coin)
    # make the timestamp for the animation
    if last_timestamp_coins is None or timestamp - last_timestamp_coins > 150:
        coins_counter += 1
        if coins_counter >= 5:
            coins_counter = 0
        last_timestamp_coins = timestamp


def draw_letters(screen: pygame.Surface, player_rect: pygame.Rect) -> None:
    """
    Draw the letters
    :param screen: pygame.Surface: where the letters should be drawn
    :param player_rect: pygame.Rect -> the rect of the player
    """
    global next_letter_idx
    # draw the letters which the player didn't collect and check for another collection
    for idx in range(next_letter_idx, len(letters)):
        letter_position = letters_position[idx]
        screen.blit(letters[idx], letter_position)

        letter_rect = pygame.Rect((letter_position[0], letter_position[1], g.POWER_UPS_SIZE, g.POWER_UPS_SIZE))
        if player_rect.colliderect(letter_rect) and idx == next_letter_idx:
            next_letter_idx += 1


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


def draw_clock(screen: pygame.Surface) -> None:
    global last_timestamp_clock, time
    timestamp = pygame.time.get_ticks()

    font = pygame.font.Font("assets/fonts/clock.otf", g.HEIGHT//30)
    time_min = time//60
    time_sek = time-time_min*60
    if time < 0:
        time_min, time_sek = 0,0
    if time_sek//10 > 0:
        text = font.render(f"0{time_min}:{time_sek}", False, "black")
    else:
        text = font.render(f"0{time_min}:0{time_sek}", False, "black")
    text_width, text_height = text.get_size()
    screen.blit(text, (g.WIDTH // 2 - text_width//2, 0))
    if timestamp - last_timestamp_clock >= 1000:
        time -= 1
        last_timestamp_clock = timestamp