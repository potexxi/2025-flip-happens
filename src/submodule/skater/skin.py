import pygame
import src.submodule.globals as s

images_push: list[pygame.Surface] = [] # Hier ist Bildliste für Animation
images_drive: list[pygame.Surface] = []
image_counter = 0 # Hier Bildindex für Animation
x_position = 0
y_position = 0
last_timestamp: float = None


# 59 x 65px = skin
def init():
    global images_push, images_drive # Hier globale Bildliste verwenden
    image = pygame.image.load('assets/player/player1.png').convert_alpha() # Bild laden
    for i in range(9):
        sub_image = image.subsurface((64 * i, 135, 60, 60))
        sub_image = pygame.transform.scale(sub_image, (s.ASSETS_SIZE, s.ASSETS_SIZE))
        #image = pygame.image.load(f"assets/player/player{i +1}.png").convert_alpha() # Hier Bilder dynamisch laden(player1, player2,....)
        images_push.append(sub_image) # Bild Hinzufügen
    for i in range(3):
        sub_image = image.subsurface((64 * i, 195, 60, 60))
        sub_image = pygame.transform.scale(sub_image, (s.ASSETS_SIZE, s.ASSETS_SIZE))
        #image = pygame.image.load(f"assets/player/player{i +1}.png").convert_alpha() # Hier Bilder dynamisch laden(player1, player2,....)
        images_drive.append(sub_image) # Bild Hinzufügen


def move(x_position, y_position):
    """
    -	Springen: Space
    -	Links: A
    -	Rechts: D
    -	Pause ESC
    """
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_SPACE]:
        pass
    elif pressed_keys[pygame.K_a]: # ( A Taste nach links gehen)
        if x_position > 0:
            x_position -= 1 # ( größer = Schneller)
            print("user pressed A ")
    elif pressed_keys[pygame.K_d]: # ( D Taste nach rechts gehen)
        if x_position > 0:
            x_position += 1
            print("user pressed D ") # (größer = Schneller)
    elif pressed_keys[pygame.K_ESCAPE]:
        pass

def draw(screen: pygame.Surface, mode: str):
    global image_counter, x_position, y_position, last_timestamp
    timestamp = pygame.time.get_ticks()
    if mode == "push":
        image = images_push[image_counter]
    else:
        image = images_drive[image_counter]
    screen.blit(image, (0,0))
    if last_timestamp is None or timestamp - last_timestamp > 100:
        image_counter += 1
        if mode == "push":
            if image_counter >= 9:
                image_counter = 0
        else:
            if image_counter >= 3:
                image_counter = 0
        last_timestamp = timestamp


if __name__ == '__main__':
    pygame.init()
    while True:
        global time_stamp_ms
        screen = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
        pygame.display.set_caption('Skin Flip')
        init()
        draw(screen)
        pygame.display.flip()



