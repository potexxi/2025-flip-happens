import pygame
import submodule.menu.menu as menu
import submodule.globals as g
import src.submodule.level1.level1 as level1


def main() -> None:
    """
    Main-funktion and entrance of the game
    """
    # Init-PyGame
    pygame.init()

    # Screen and Caption
    pygame.display.set_caption("Flip Happens")
    screen = pygame.display.set_mode((0, 0))

    clock = pygame.time.Clock()


    # Initialization
    menu.init_background()
    level1.init_level1()

    mode = "menu"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if mode == "menu":
            mode = menu.menu(screen)

        if mode == "play":
            mode = level1.level1(screen)

        if mode == "explain":
            # Todo: Explain
            pass

        if mode == "pause":
            # TODO:Pause
            screen.fill("white")
            pass


        # Update the display
        pygame.display.flip()
        # An die FPS anpassen
        clock.tick(g.FPS)
    # Pygame immer sauber beenden
    pygame.quit()



if __name__ == "__main__":
    main()
