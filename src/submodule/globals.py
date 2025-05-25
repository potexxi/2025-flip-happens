import pygame
import math

pygame.init()

# Height and Width of the window
HEIGHT = int(pygame.display.Info().current_h)
WIDTH = int(pygame.display.Info(). current_w)

# Size of ASSETS
ASSETS_SIZE = int(pygame.display.Info().current_h // 16)
POWER_UPS_SIZE = int(ASSETS_SIZE//2.7)
PLAYER_SIZE = ASSETS_SIZE
KEY_SIZE = ASSETS_SIZE // 1.1

# On which position the background-picture is
POSITION_WORLD = [0,0]

# The speed of the player in px
SPEED = (3.5 * ASSETS_SIZE) / 65
RAMP_SPEED = SPEED
RAMP_JUMP = math.sqrt(2 * 0.5 * ASSETS_SIZE) + 3
RAMP_JUMP2 = RAMP_JUMP - 5

# Gravity
GRAVITATION = 0.5
JUMP = math.sqrt(2 * GRAVITATION * ASSETS_SIZE) + 1
MAX_FALL_SPEED = 10




FPS = 65
