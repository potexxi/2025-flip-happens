import pygame
import submodule.menu as menu


def main():
    """
    Main-funktion
    """
    # Init-PyGame
    pygame.init()

    # Screen and Caption
    pygame.display.set_caption("Flip Happens")
    screen = pygame.display.set_mode((0, 0))


    # Initialization
    menu.init_background()

    mode = "menu"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if mode == "menu":
            menu.menu(screen)

        if mode == "play":
            screen.fill("white")

        if mode == "explain":
            screen.fill("white")


        # Update the display
        pygame.display.flip()
        pygame.display.update()



if __name__ == "__main__":
    main()