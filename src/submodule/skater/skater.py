import pygame
import src.submodule.globals as g
from src.submodule.level1.place_blocks import blocks

images_drive_left: list[pygame.Surface] = []
images_drive_right: list[pygame.Surface] = []
images_left: list[pygame.Surface] = []
images_right: list[pygame.Surface] = []
image_counter = 0
x_position = 0
y_position = 0
last_timestamp = None
last_direction: str = "right"
velocity: list[float] = [0,0]


def init():
    # normal fahren
    #image = pygame.image.load('assets/player/player1.png').convert_alpha() # Bild laden
    #for i in range(3):
      #  sub_image = image.subsurface((64 * i, 195, 60, 60))
     #   sub_image = pygame.transform.scale(sub_image, (g.ASSETS_SIZE, g.ASSETS_SIZE))
     #   images_drive_left.append(sub_image) # Bild Hinzufügen
    #for image in images_drive_left:
       # image = pygame.transform.flip(image, g.ASSETS_SIZE,0)
       # images_drive_right.append(image)

    # mit anschubsen
    image = pygame.image.load('assets/player/player1.png').convert_alpha()  # Bild laden
    for i in range(9):
        sub_image = image.subsurface((64 * i, 135, 60, 60))
        sub_image = pygame.transform.scale(sub_image, (g.ASSETS_SIZE, g.ASSETS_SIZE))
        # image = pygame.image.load(f"assets/player/player{i +1}.png").convert_alpha() # Hier Bilder dynamisch laden(player1, player2,....)
        images_left.append(sub_image)  # Bild Hinzufügen
    for image in images_left:
        image = pygame.transform.flip(image, g.ASSETS_SIZE,0)
        images_right.append(image)


def move() -> None:
    """
    Moves the player and checks if the player dashes in something
    """
    global x_position, y_position, last_direction, velocity
    skater_rect = pygame.Rect(x_position, y_position, g.ASSETS_SIZE, g.ASSETS_SIZE)
    pressed_keys = pygame.key.get_pressed()
    direction = last_direction
    jump = False
    if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
        direction = "left"
    if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
        direction = "right"
    if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_UP]:
        jump = True

    # Moves the player automatically to the right or the left
    if direction == "right" and x_position <= g.WIDTH-g.ASSETS_SIZE:
        x_position += g.SPEED
    if direction == "left" and x_position >= 0:
        x_position -= g.SPEED
    last_direction = direction

    platform_collide = False
    # Check if the player is on a platform
    for block in blocks:
        if pygame.Rect(skater_rect).colliderect(pygame.Rect((block[0], block[1], block[2], block[3]))):
            platform_collide = True

    # Gravity
    if not(platform_collide):
        velocity[1] += g.GRAVITATION
        if jump:
            velocity[1] = -g.JUMP
        y_position += velocity[1]

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
            if y_position + g.ASSETS_SIZE <= block[3] + 10 and velocity[1] >= 0:
                on_platform = True
                y_position = block[3] - g.ASSETS_SIZE  # Position korrigieren
                velocity[1] = 0
                break
    # Springen nur, wenn auf Plattform
    if on_platform and jump:
        velocity[1] = -g.JUMP

    # Schwerkraft anwenden
    if not on_platform:
        velocity[1] = min(velocity[1] + g.GRAVITATION, g.MAX_FALL_SPEED)
        y_position += velocity[1]
    # KI-Ende




def draw(screen: pygame.Surface):
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




