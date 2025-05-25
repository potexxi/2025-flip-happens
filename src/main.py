import pygame
import submodule.menu.menu as menu
import submodule.globals as g
import src.submodule.explain_menu.explain_menu as explain
import src.submodule.level1.play as level1
import src.submodule.skater.skater as player
import src.submodule.pause_menu.pause as pause
import src.submodule.start_animation.start_animation as start
from src.submodule.level1.place_blocks import init_blocks
from src.submodule.level1.place_assets import init_assets


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
    init_blocks()
    init_assets()
    player.init()
    start.init()
    pause.init()

    mode = "play"
    animation = True

    esc_pressed = False

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    esc_pressed = True
                if mode == "start":
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        mode = "menu"


        if mode == "start":
            animation, mode = start.animation(screen, animation)

        if mode == "menu":
            mode = menu.menu(screen)

        if mode == "play":
            mode = level1.play(screen, events)
            if mode == "pause":
                esc_pressed = False
                clock.tick(g.FPS)
                pygame.display.flip()
                continue

        if mode == "explain":
            mode = explain.menu(screen)

        if mode == "pause":
            mode = pause.pause(screen, esc_pressed, events)


        # Update the display
        pygame.display.flip()
        # An die FPS anpassen
        clock.tick(g.FPS)
    # Pygame immer sauber beenden
    pygame.quit()



if __name__ == "__main__":
    main()
