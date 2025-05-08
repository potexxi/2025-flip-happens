import pygame
import submodule.globals as g


def main():
    """
    Main-funktion
    """

    # Initialization
    pygame.init()

    # Screen and Caption
    screen = pygame.display.set_mode((g.WIDTH, g.HEIGHT))
    pygame.display.set_caption("Flip Happens")

    running = True
    while running:
        pass
        # Todo: weitermachen



if __name__ == "__main__":
    main()