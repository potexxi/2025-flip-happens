import pygame
import submodule.menu as menu
import submodule.globals as g
import submodule.explain_menu as explain
import submodule.levels.level1 as level1


def main():
    """
    Main-funktion
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
            explain.explain_menu(screen)


        # Update the display
        pygame.display.flip()

        clock.tick(g.FPS)



if __name__ == "__main__":
    main()