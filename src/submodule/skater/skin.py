import pygame
import src.submodule.globals as s

images: list[pygame.Surface] = [] # Hier ist Bildliste für Animation
image_counter = 0 # Hier Bildindex für Animation
x_position = 0
y_position = 0
time_stamp: float = None


# 59 x 65px = skin
def init():
    global images # Hier globale Bildliste verwenden
    image = pygame.image.load('player1.png').convert_alpha() # Bild laden
    for i in range(3):
        sub_image = image.subsurface((59 * i, 192, 59, 65))
        sub_image = pygame.transform.scale(sub_image, (s.ASSETS_SIZE, s.ASSETS_SIZE))
        #image = pygame.image.load(f"assets/player/player{i +1}.png").convert_alpha() # Hier Bilder dynamisch laden(player1, player2,....)
        images.append(sub_image) # Bild Hinzufügen


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

def draw(screen: pygame.Surface):
    global image_counter, x_position, y_position
    frame = images[image_counter % len(images)]  # Aktuelles Bild aus der Liste
    screen.blit(frame, (x_position, y_position)) # Bild zeichnen

if __name__ == '__main__':
    pygame.init()
    timestamp_ms = pygame.time.get_ticks()
    while True:
        global time_stamp_ms
        screen = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
        pygame.display.set_caption('Skin Flip')
        init()
        draw(screen)
        pygame.display.flip()
        if (time_stamp == None or (timestamp_ms - time_stamp > 100)):
            image_counter = (image_counter + 1) % 4
            time_stamp = timestamp_ms



