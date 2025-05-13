import pygame
import submodule.menu.menu as menu
import submodule.globals as g
import submodule.level1.level1 as level1
import submodule.skater.skin as skin

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
    skin.init()


    mode = "menu"

    running = True
    while running:
        skin.draw(screen)
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
            pass


        # Update the display
        pygame.display.flip()

        clock.tick(g.FPS)



if __name__ == "__main__":
    main()
