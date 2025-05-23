import pygame

pygame.init()

# Height and Width of the window
HEIGHT = int(pygame.display.Info().current_h)
WIDTH = int(pygame.display.Info(). current_w)

# Size of ASSETS
ASSETS_SIZE = int(pygame.display.Info().current_h // 16)
POWER_UPS_SIZE = int(ASSETS_SIZE//2.7)
PLAYER_SIZE = ASSETS_SIZE

# On which position the background-picture is
POSITION_WORLD = [0,0]

# The speed of the player in px
SPEED = 4

# Gravity
GRAVITATION = 0.5
JUMP = ASSETS_SIZE//6.5
MAX_FALL_SPEED = 10



FPS = 65
