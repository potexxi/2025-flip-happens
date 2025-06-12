import pygame
import math

pygame.init()

# Height and Width of the window
HEIGHT: int = int(pygame.display.Info().current_h)
WIDTH: int = int(pygame.display.Info().current_w)

# Size of ASSETS
ASSETS_SIZE: int = int(pygame.display.Info().current_h // 16)
POWER_UPS_SIZE: int = int(ASSETS_SIZE//2.7)
PLAYER_SIZE: float = ASSETS_SIZE
KEY_SIZE: float = ASSETS_SIZE // 1.1

# On which position the background-picture is
POSITION_WORLD: list[int] = [0,0]

# The speed of the player in px
SPEED: float = (3.5 * ASSETS_SIZE) / 65
RAMP_SPEED: float = SPEED
RAMP_JUMP: float = math.sqrt(2 * 0.5 * ASSETS_SIZE) + 3
RAMP_JUMP2: float = RAMP_JUMP - 5

# Gravity
GRAVITATION: float = 0.5
JUMP: float = math.sqrt(2 * GRAVITATION * ASSETS_SIZE) + 1
MAX_FALL_SPEED: int = 10

# Shop details
USERNAME: str = ...
COINS: int = 0
COINSM: float = 1.0
SPEEDM: float = 1.0
IMMUNITY: bool = False

# Active level
LEVEL = ...

# Where the ranked.txt is saved
save: str = "submodule/menu/ranked.txt"


FPS = 65
