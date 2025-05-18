import pygame

pygame.init()

# Height and Width of the window
HEIGHT = int(pygame.display.Info().current_h)
WIDTH = int(pygame.display.Info(). current_w)

# Size of ASSETS
ASSETS_SIZE = int(pygame.display.Info().current_h // 16)
POWER_UPS_SIZE = int(ASSETS_SIZE//2.7)

WORLD_MOVE_X_PX = 0.4

SCREEN_SIZE = 128



FPS = 65
