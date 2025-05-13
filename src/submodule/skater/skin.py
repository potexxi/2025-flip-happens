import pygame
import src.submodule.globals as s

images: list[pygame.Surface] = [] # Hier ist Bildliste für Animation
image_counter = 0 # Hier Bildindex für Animation
x_position = 25
y_position = 25


def init():
    global images # Hier globale Bildliste verwenden
    image = pygame.image.load('assets/player/player1.png').convert_alpha() # Bild laden
    for i in range(5):
        image = pygame.image.load(f"assets/player/player{i +1}.png").convert_alpha() # Hier Bilder dynamisch laden(player1, player2,....)
        images.append(image) # Bild Hinzufügen


def move(x_position, y_position):
    """
    -	Springen: Space
    -	Links: A
    -	Rechts: D
    -	Pause: ESC
    """
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_SPACE]:
        pass
    elif pressed_keys[pygame.K_a]: # ( A Taste nach links gehen)
        if x_position > 0:
            x_position -= 1 # ( größer = Schneller)
            print("user pressed A ")
    elif pressed_keys[pygame.K_d]: # ( D Taste nach rechts gehen)
        if y_position > 0:
            y_position += 1
            print("user pressed D ") # (größer = Schneller)
    elif pressed_keys[pygame.K_ESCAPE]:
        pass


