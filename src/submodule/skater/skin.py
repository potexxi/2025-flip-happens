import pygame
import src.submodule.globals as g

images_drive_left: list[pygame.Surface] = []
images_drive_right: list[pygame.Surface] = []
image_counter = 0
x_position = 0
y_position = 0
last_timestamp = None
last_direction: str = "right"



# 59 x 65px = skin
def init():
    global images_drive_left # Hier globale Bildliste verwenden
    image = pygame.image.load('assets/player/player1.png').convert_alpha() # Bild laden
    for i in range(3):
        sub_image = image.subsurface((64 * i, 195, 60, 60))
        sub_image = pygame.transform.scale(sub_image, (g.ASSETS_SIZE, g.ASSETS_SIZE))
        images_drive_left.append(sub_image) # Bild Hinzufügen
    for image in images_drive_left:
        image = pygame.transform.flip(image, 0,0)
        images_drive_right.append(image)


def move() -> None:
    """
    Moves the player and checks if the player dashes in something
    """
    global x_position, y_position, last_direction
    pressed_keys = pygame.key.get_pressed()
    direction = last_direction
    if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
        direction = "left"
    if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
        direction = "right"

    # Moves the player automatically to the right or the left
    if direction == "right":
        x_position += g.SPEED
    if direction == "left":
        x_position -= g.SPEED
    last_direction = direction


def draw(screen: pygame.Surface):
    global image_counter, last_timestamp
    timestamp = pygame.time.get_ticks()
    image = images_drive_right[image_counter]

    screen.blit(image, (x_position,y_position))
    if last_timestamp is None or timestamp - last_timestamp > 150:
        image_counter += 1
        if image_counter >= len(images_drive_right):
            image_counter = 0
        last_timestamp = timestamp




