import pygame
import random
import src.submodule.globals as g

images_drive_left: list[pygame.Surface] = []
images_drive_right: list[pygame.Surface] = []
images_left: list[pygame.Surface] = []
images_right: list[pygame.Surface] = []
image_counter: int = 0
x_position: float = 0
y_position: float = g.HEIGHT - 2 * g.PLAYER_SIZE
last_timestamp: int = None
last_direction: str = "right"
velocity: list[float] = [0,0]
big_speed: bool = False
big_jump: bool = False
speed: float = g.SPEED
jump_px: float = g.JUMP
last_timestamp_speed: int = 0
last_timestamp_jump: int = 0
power_up_start_time: int = 0
power_up: bool = False
blocks: list[tuple] = []
poles: list[tuple] = []
halfpipes_right: list[tuple] = []
halfpipes_left: list[tuple] = []
fast_ramp: list[tuple] = []
high_ramps_right: list[tuple] = []
high_ramps_left: list[tuple] = []


def init() -> None:
    """
    Init the pictures of the player out of the sprite
    """
    # normal fahren
    #image = pygame.image.load('assets/player/player1.png').convert_alpha() # Bild laden
    #for i in range(3):
        #sub_image = image.subsurface((64 * i, 195, 60, 60))
        #sub_image = pygame.transform.scale(sub_image, (g.ASSETS_SIZE, g.ASSETS_SIZE))
        #images_drive_left.append(sub_image) # Bild Hinzufügen
    #for image in images_drive_left:
        #image = pygame.transform.flip(image, True,False)
        #images_drive_right.append(image)

    # mit anschubsen
    image = pygame.image.load('assets/player/player1.png').convert_alpha()  # Bild laden
    for i in range(9):
        sub_image = image.subsurface((64 * i, 135, 60, 60))
        sub_image = pygame.transform.scale(sub_image, (g.PLAYER_SIZE, g.PLAYER_SIZE))
        # image = pygame.image.load(f"assets/player/player{i +1}.png").convert_alpha() # Hier Bilder dynamisch laden(player1, player2,....)
        images_left.append(sub_image)  # Bild Hinzufügen
    for image in images_left:
        image = pygame.transform.flip(image, True,False)
        images_right.append(image)


def move(rain: bool) -> None:
    """
    Moves the player and checks if the player dashes in something
    :param rain: True -> it is raining, False -> it is not raining
    """
    global x_position, y_position, last_direction, velocity, big_speed, last_timestamp_speed, speed, power_up
    global power_up_start_time
    skater_rect = pygame.Rect(x_position, y_position, g.PLAYER_SIZE, g.PLAYER_SIZE)
    pressed_keys = pygame.key.get_pressed()
    direction = last_direction
    timestamp = pygame.time.get_ticks()
    jump = False
    if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
        direction = "left"
    if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
        direction = "right"
    if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_UP]:
        jump = True
    if big_speed:
        speed = g.RAMP_SPEED
    else:
        speed = g.SPEED

    # Check if the player has a power up
    if power_up:
        speed += 4/g.SPEEDM
        if timestamp - power_up_start_time > 5000:
            power_up = False

    # Check if the player drives in a block or a pole
    for block in blocks:
        block_rect = pygame.Rect(block[2], block[3], block[0], block[1])
        if skater_rect.colliderect(block_rect):
            if direction == "right":
                if skater_rect.right <= block_rect.left + 10:
                    speed = 0
                    break
            if direction == "left":
                if skater_rect.left >= block_rect.right - 10:
                    speed = 0
                    break

    for pole in poles:
        pole_rect = pygame.Rect(pole[2], pole[3], pole[0], pole[1]//2)
        if skater_rect.colliderect(pole_rect):
            if direction == "right":
                if skater_rect.right <= pole_rect.left + 10:
                    speed = 0
                    break
            if direction == "left":
                if skater_rect.left >= pole_rect.right - 10:
                    speed = 0
                    break

    # Check if the player drives on a ramp
    if not big_speed:
        for ramp in fast_ramp:
            ramp_rect = pygame.Rect(ramp[2], ramp[3], ramp[0], ramp[1])
            if skater_rect.colliderect(ramp_rect):
                if g.RAMP_SPEED == g.SPEED:
                    if speed < 6:
                        g.RAMP_SPEED += 6
                    else:
                        speed += 2
                big_speed = True
                speed = g.RAMP_SPEED
                last_timestamp_speed = timestamp
                break

    if direction == "left":
        for halfpipe in halfpipes_left:
            ramp_rect = pygame.Rect(halfpipe[2], halfpipe[3]
                                    ,halfpipe[0] - g.PLAYER_SIZE//1.5, halfpipe[1])
            if skater_rect.colliderect(ramp_rect):
                velocity[1] = -g.RAMP_JUMP
                break
        for ramp in high_ramps_right:
            ramp_rect = pygame.Rect(ramp[2], ramp[3], ramp[0], ramp[1])
            if skater_rect.colliderect(ramp_rect):
                velocity[1] = -g.RAMP_JUMP2
                if g.RAMP_SPEED == g.SPEED:
                    g.RAMP_SPEED += 5
                big_speed = True
                speed = g.RAMP_SPEED
                last_timestamp_speed = timestamp
                break

    if direction == "right":
        for halfpipe in halfpipes_right:
            ramp_rect = pygame.Rect(halfpipe[2] + g.PLAYER_SIZE//1.5, halfpipe[3],
                                    halfpipe[0] - g.PLAYER_SIZE//1.5, halfpipe[1])
            if skater_rect.colliderect(ramp_rect):
                velocity[1] = -g.RAMP_JUMP
                break
        for ramp in high_ramps_left:
            ramp_rect = pygame.Rect(ramp[2], ramp[3] + (ramp[1]//2), ramp[0], ramp[1]//2)
            if skater_rect.colliderect(ramp_rect):
                velocity[1] = -g.RAMP_JUMP2
                if g.RAMP_SPEED == g.SPEED:
                    g.RAMP_SPEED += 5
                big_speed = True
                speed = g.RAMP_SPEED
                last_timestamp_speed = timestamp
                break

    # Regen machen
    if not g.IMMUNITY:
        if rain:
            if random.random() < 0.5: # yamen: hier mache ich mit 0,5 die 50 % wahrscheinlichkeit
                                      # und random.random() gibt eine gleitkommazahl zwischen 0 und 1
                jump = False
                if random.random() < 0.01: # hier auch yamen, halt mit 1 % wahrscheinlichkeit
                    if random.randint(1,2) == 1:
                        direction = "right"
                    else:
                        direction = "left"
            multiplier = random.uniform(0.5, 1.5) # yamen: uniform bedeutet, dass nicht wie bei random.randint
                                                             # eine int zahl kommt, sondern eine float zahl
            speed *= multiplier

    # Moves the player automatically to the right or the left
    speed *= g.SPEEDM
    if direction == "right" and x_position <= g.WIDTH - g.ASSETS_SIZE:
        x_position += speed
    if direction == "left" and x_position >= 0:
        x_position -= speed
    last_direction = direction

    # KI-Anfang:
    # KI: ChatGPT
    # prompt: fixe die Funktion: platform_collide = False
    #     # Check if the player is on a platform
    #     for block in blocks:
    #         if pygame.Rect(skater_rect).colliderect(pygame.Rect((block[0], block[1], block[2], block[3]))):
    #             platform_collide = True
    #
    #     # Gravity
    #     if not(platform_collide):
    #         velocity[1] += g.GRAVITATION
    #         if jump:
    #             velocity[1] = -g.JUMP
    #         y_position += velocity[1]
    on_platform = False
    for block in blocks:
        block_rect = pygame.Rect(block[2], block[3], block[0], block[1])
        # Prüfe nur Boden-Kollision (unter dem Spieler)
        if skater_rect.colliderect(block_rect):
            # Prüfe, ob Spieler genau auf dem Block steht (z. B. Kollision von unten)
            # Spieler muss sich von oben nähern und darf nicht weit rechts/links daneben sein
            if (block_rect.top <= skater_rect.bottom and skater_rect.bottom <= block_rect.top + 10 and
                    velocity[1] >= 0 and skater_rect.right > block_rect.left + 5 and
                    skater_rect.left < block_rect.right - 5):
                on_platform = True
                y_position = block[3] - g.PLAYER_SIZE # Position korrigieren
                velocity[1] = 0
                break
    on_pole = False
    for pole in poles:
        pole_rect = pygame.Rect(pole[2], pole[3], pole[0], pole[1])
        # Prüfe nur Boden-Kollision (unter dem Spieler)
        if skater_rect.colliderect(pole_rect):
            # Prüfe, ob Spieler genau auf dem Block steht (z. B. Kollision von unten)
            if (pole_rect.top <= skater_rect.bottom and skater_rect.bottom <= pole_rect.top + 10 and
                    velocity[1] >= 0 and skater_rect.right > pole_rect.left + 5 and
                    skater_rect.left < pole_rect.right - 5):
                on_pole = True
                y_position = pole[3] - g.PLAYER_SIZE  # Position korrigieren
                velocity[1] = 0
                break
    # Springen nur, wenn auf Plattform
    if (on_platform or on_pole) and jump:
        velocity[1] = -g.JUMP

    # Schwerkraft anwenden
    if not on_platform and not on_pole:
        velocity[1] = min(velocity[1] + g.GRAVITATION, g.MAX_FALL_SPEED)
        y_position += velocity[1]
    # KI-Ende

    # disable the big speed, when the time is over
    if big_speed:
        if timestamp - last_timestamp_speed > 200:
            big_speed = False

    # check, if above the player a block or pole is
    skater_top_rect = pygame.Rect(x_position, y_position, g.PLAYER_SIZE, 5)
    for block in blocks:
        block_rect = pygame.Rect(block[2] + (block[0] - block[0]/1.5)/2, block[3], block[0]/1.5, block[1])
        if skater_top_rect.colliderect(block_rect) and velocity[1] < 0:
            velocity[1] = 0
            break
    for pole in poles:
        pole_rect = pygame.Rect(pole[2] + (pole[0] - pole[0]/1.5)/2, pole[3], pole[0]/1.5, pole[1]//2)
        if skater_top_rect.colliderect(pole_rect) and velocity[1] < 0:
            velocity[1] = 0
            break


def draw(screen: pygame.Surface) -> None:
    """
    Draw the player pictures
    :param screen: pygame.Surface -> where the pictures shall be drawn
    """
    global image_counter, last_timestamp
    timestamp = pygame.time.get_ticks()
    if last_direction == "right":
        image = images_right[image_counter]
    else:
        image = images_left[image_counter]

    screen.blit(image, (x_position,y_position))
    if last_timestamp is None or timestamp - last_timestamp > 100:
        image_counter += 1
        if image_counter >= len(images_right):
            image_counter = 0
        last_timestamp = timestamp
