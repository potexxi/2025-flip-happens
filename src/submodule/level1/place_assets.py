import copy
import pygame
import submodule.globals as g
import submodule.level1.play as play1
import submodule.skater.skater as player
import submodule.level2.play as play2


background: pygame.Surface = ...
brick: pygame.Surface = ...
ui_pause: pygame.Surface = ...
halfpipes: list[pygame.Surface] = []
pipe: pygame.Surface = ...
fast_ramp: pygame.Surface = ...
music: pygame.mixer.Sound = ...
coin: pygame.mixer.Sound = ...
powerup: pygame.mixer.Sound = ...
letter: pygame.mixer.Sound = ...
high_ramps: list[pygame.Surface] = []
coins: list[pygame.Surface] = []
letters: list[pygame.Surface] = []
power_up: list[pygame.Surface] = []
you_won: pygame.Surface = ...
you_lost: pygame.Surface = ...
coins_counter: int = 0
power_counter: int = 0
last_timestamp_coins: int = None
last_timestamp_power: int = None
last_timestamp_clock: int = 0
time: int = 105
first_block_floor: tuple[float,float] = (-30, g.HEIGHT - (g.ASSETS_SIZE - g.ASSETS_SIZE // 2) - g.ASSETS_SIZE)
first_asset: tuple[float,float] = (first_block_floor[0] + (g.ASSETS_SIZE - g.POWER_UPS_SIZE) / 2,
    first_block_floor[1] + (g.ASSETS_SIZE//2.5))
first_power_up: tuple[float,float] = (first_asset[0] - g.POWER_UPS_SIZE//4, first_asset[1] - g.POWER_UPS_SIZE//2)
append_elements: bool = True
collectables_original = [
    [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,3,0,0,2,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,3,3,3,4,4,4,4,0,0,1,1,1,0,0,0,0,0,8,1,1,0,0],
    [3,3,1,1,1,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,0,0,0,3,3,3,3,3],
    [0,0,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3],
    [0,0,0,0,0,4,4,3,0,0,0,0,0,0,0,0,0,0,1,1,1,0,5,3,3,3,3,3,3],
    [3,3,6,0,0,0,0,3,3,6,0,7,0,0,0,4,4,0,4,4,4,3,3,3,3,3,3,3,3],
    [3,3,3,3,0,0,0,0,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,4,0,0,0,0,0,0,0,0,3,3,3,0,0,8,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,3,3,3,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,5,0,0,1,1,1,7,2,0,1,1,1,5,3,0,0,0,0,4,4,4,0,1,0],
    [3,3,3,3,3,4,4,4,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,4,4,4,0,0],
    [0,0,1,1,1,1,0,0,0,8,0,9,0,0,1,1,1,1,0,0,4,4,4,4,0,0,0,0,0],
    [4,4,4,4,4,4,4,0,0,3,3,3,0,0,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,5,3,3,3,6,0,1,1,1,1,2,1,1,1,1,0,0,0,0,0,0],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
]
collectables = copy.deepcopy(collectables_original)
collectables.reverse()
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
    Init the pictures, which the game needs
    """
    global coins, letters, power_up, you_won, you_lost, background, brick, halfpipes, fast_ramp, high_ramps, pipe, music
    global coin, powerup, letter
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

    # Won and Lose Picture:
    you_won = pygame.image.load("assets/level1/you_won.png").convert_alpha()
    you_won = pygame.transform.scale(you_won, (g.WIDTH // 2, g.WIDTH//2))
    you_lost = pygame.image.load("assets/level1/you_lost.png").convert_alpha()
    you_lost = pygame.transform.scale(you_lost, (g.WIDTH // 2, g.WIDTH // 2))

    # Background:
    background = pygame.image.load("assets/level1/background.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))

    # Brick:
    brick = pygame.image.load("assets/level1/BrickTiles.png").convert_alpha()
    brick = brick.subsurface((0, 0, 16, 16))
    brick = pygame.transform.scale(brick, (g.ASSETS_SIZE, g.ASSETS_SIZE))

    # Halfpipe:
    halfpipe_left = pygame.image.load("assets/level1/halfpipe.png")
    halfpipe_left = pygame.transform.scale(halfpipe_left, (g.ASSETS_SIZE, g.ASSETS_SIZE))
    halfpipes.append(halfpipe_left)
    halfpipe_right = pygame.transform.flip(halfpipe_left, True, False)
    halfpipes.append(halfpipe_right)

    # Pipe:
    pipe = pygame.image.load("assets/level1/pipe.png").convert_alpha()
    pipe = pygame.transform.scale(pipe, (g.ASSETS_SIZE, g.ASSETS_SIZE))

    # Ramps:
    high_ramp_left = pygame.image.load("assets/level1/high_ramp_left.png").convert_alpha()
    high_ramp_left = pygame.transform.scale(high_ramp_left, (g.ASSETS_SIZE, g.ASSETS_SIZE))
    high_ramps.append(high_ramp_left)
    high_ramp_right = pygame.image.load("assets/level1/high_ramp_right.png").convert_alpha()
    high_ramp_right = pygame.transform.scale(high_ramp_right, (g.ASSETS_SIZE, g.ASSETS_SIZE))
    high_ramps.append(high_ramp_right)
    fast_ramp = pygame.image.load("assets/level1/wide_ramp.png").convert_alpha()
    fast_ramp = pygame.transform.scale(fast_ramp, (g.ASSETS_SIZE, g.ASSETS_SIZE))

    # Music
    music = pygame.mixer.Sound("assets/sounds/level1.mp3")
    music.set_volume(0.3)
    coin = pygame.mixer.Sound("assets/sounds/coin.mp3")
    powerup = pygame.mixer.Sound("assets/sounds/powerup.wav")
    powerup.set_volume(0.6)
    letter = pygame.mixer.Sound("assets/sounds/letter.wav")


def check_for_collect(type_: int, player_rect: pygame.Rect, x_position: float, y_position: float) -> bool:
    """
    Check if a coin or power ups gets collected by the player
    :param type_: 1 -> Coin, 2 -> Power Up
    :param player_rect: the pygame.Rect of the player
    :param x_position: the x-koordinate of the collectable
    :param y_position: the y-koordinate of the collectable
    :return: True -> the player collects, False -> the player doesn't collect
    """
    if type_ == 1:
        coin_rect = pygame.Rect((x_position, y_position, g.POWER_UPS_SIZE, g.POWER_UPS_SIZE))
        if player_rect.colliderect(coin_rect):
            coin.play()
            if g.LEVEL == "level1":
                play1.coins_collected += 1
            if g.LEVEL == "level2":
                play2.coins_collected += 1
            return True
    if type_ == 2:
        power_rect = pygame.Rect((x_position, y_position, g.POWER_UPS_SIZE, g.POWER_UPS_SIZE))
        if player_rect.colliderect(power_rect):
            powerup.play()
            player.power_up = True
            player.power_up_start_time = pygame.time.get_ticks()
            return True
    return False


def draw_assets(screen: pygame.Surface, player_rect: pygame.Rect) -> None:
    """
    Go through the defined matrix with the collectables and blit them
    :param screen: pygame.Surface -> where the collectables shall be drawn
    :param player_rect: the pygame.Rect of the player
    """
    global last_timestamp_coins, last_timestamp_power, coins_counter, power_counter, append_elements
    timestamp = pygame.time.get_ticks()
    for y, line in enumerate(collectables):
        for x, item in enumerate(line):
            x_position = first_block_floor[0] + x * g.ASSETS_SIZE
            y_position = (first_block_floor[1] + g.ASSETS_SIZE) - y * g.ASSETS_SIZE
            if item == 1:
                x_position = first_asset[0] + x * g.ASSETS_SIZE
                y_position = first_asset[1] - (y-1) * g.ASSETS_SIZE
                screen.blit(coins[coins_counter], (x_position, y_position))
                if check_for_collect(item, player_rect, x_position, y_position):
                    collectables[y][x] = 0

            elif item == 2:
                x_position = first_power_up[0] + x * g.ASSETS_SIZE
                y_position = first_power_up[1] - (y-1) * g.ASSETS_SIZE
                screen.blit(power_up[power_counter], (x_position, y_position))
                if check_for_collect(item, player_rect, x_position, y_position):
                    collectables[y][x] = 0

            if item == 3:
                screen.blit(brick, (x_position, y_position))
                if append_elements:
                    player.blocks.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 4:
                screen.blit(pipe, (x_position, y_position))
                if append_elements:
                    player.poles.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 5:
                screen.blit(halfpipes[0], (x_position, y_position))
                if append_elements:
                    player.halfpipes_right.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 6:
                screen.blit(halfpipes[1], (x_position, y_position))
                if append_elements:
                    player.halfpipes_left.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 7:
                screen.blit(fast_ramp, (x_position, y_position))
                if append_elements:
                    player.fast_ramp.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 8:
                screen.blit(high_ramps[1], (x_position, y_position))
                if append_elements:
                    player.high_ramps_right.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

            if item == 9:
                screen.blit(high_ramps[0], (x_position, y_position))
                if append_elements:
                    player.high_ramps_left.append((g.ASSETS_SIZE, g.ASSETS_SIZE, x_position, y_position))

    append_elements = False

    # Doing the sprite stuff for the next pictures
    if last_timestamp_coins is None or timestamp - last_timestamp_coins > 150:
        coins_counter += 1
        if coins_counter >= 5:
            coins_counter = 0
        last_timestamp_coins = timestamp
    if last_timestamp_power is None or timestamp - last_timestamp_power > 200:
        power_counter += 1
        if power_counter >= 4:
            power_counter = 0
        last_timestamp_power = timestamp


def draw_letters(screen: pygame.Surface, player_rect: pygame.Rect, _letters_position: list[tuple]) -> None:
    """
    Blit the letters at their positions, the positions are defined already
    :param screen: pygame.Surface: where the letters should be drawn
    :param player_rect: pygame.Rect -> the rect "hit box" of the player
    :param _letters_position: letters position
    """
    global next_letter_idx
    # draw the letters which the player didn't collect and check for another collection
    for idx in range(next_letter_idx, len(letters)):
        letter_position = _letters_position[idx]
        screen.blit(letters[idx], letter_position)

        letter_rect = pygame.Rect((letter_position[0], letter_position[1], g.POWER_UPS_SIZE, g.POWER_UPS_SIZE))
        if player_rect.colliderect(letter_rect) and idx == next_letter_idx:
            letter.play()
            if g.LEVEL == "level1":
                play1.letters_collected += 1
            else:
                play2.letters_collected += 1
            next_letter_idx += 1


def draw_clock(screen: pygame.Surface, _time: int) -> int:
    """
    Draw the left time on the screen (up, middle)
    :param screen: pygame.Surface -> where the clock shall be drawn
    :param _time: the left time in seconds
    :return: how much time is left
    """
    global last_timestamp_clock

    timestamp = pygame.time.get_ticks()
    font = pygame.font.Font("assets/fonts/clock.otf", g.HEIGHT//30)
    time_min = _time//60
    time_sek = _time-time_min*60
    if _time < 0:
        time_min, time_sek = 0,0
    if time_sek//10 > 0:
        text = font.render(f"0{time_min}:{time_sek}", False, "black")
    else:
        text = font.render(f"0{time_min}:0{time_sek}", False, "black")
    text_width, text_height = text.get_size()
    screen.blit(text, (g.WIDTH // 2 - text_width//2, 0))
    if timestamp - last_timestamp_clock >= 1000:
        _time -= 1
        last_timestamp_clock = timestamp
    return _time