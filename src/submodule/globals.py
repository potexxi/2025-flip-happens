import pygame

pygame.init()

# Height and Width of the window
HEIGHT = int(pygame.display.Info().current_h)
WIDTH = int(pygame.display.Info(). current_w)

# Size of ASSETS
ASSETS_SIZE = int(pygame.display.Info().current_h // 16)
POWER_UPS_SIZE = int(ASSETS_SIZE//2.7)

# How fast the World moves in the start menu
WORLD_MOVE_X_PX = 0.3

# The speed of the player in px
SPEED = HEIGHT//(HEIGHT//3)

# Gravity
GRAVITATION = 0.5
JUMP = HEIGHT//125
MAX_FALL_SPEED = 10



FPS = 65
