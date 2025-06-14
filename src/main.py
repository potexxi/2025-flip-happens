import pygame
import submodule.menu.menu as menu
import submodule.globals as g
import submodule.explain_menu.explain_menu as explain
import submodule.level1.play as level1
import submodule.level2.play as level2
import submodule.skater.skater as player
import submodule.pause_menu.pause as pause
import submodule.start_animation.start_animation as start
import submodule.shop.shop as shop
from submodule.level1.place_assets import init_assets as init_assets1
from submodule.level2.place_assets import init_assets as init_assets2
from submodule.rain.rain import init as init_rain


def main() -> None:
    """
    Main-funktion and entrance of the game, game loop
    """
    # Init-PyGame
    pygame.init()
    pygame.mixer.init()

    # Screen and Caption
    pygame.display.set_caption("Flip Happens")
    screen = pygame.display.set_mode((0, 0))

    clock = pygame.time.Clock()


    # Initialization
    menu.init()
    init_assets1()
    init_assets2()
    player.init()
    start.init()
    pause.init()
    init_rain()
    shop.init()

    mode = "start"

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
            mode = start.animation(screen, events)

        if mode == "menu":
            mode = menu.menu(screen, events)

        if mode == "level1":
            g.LEVEL = "level1"
            mode = level1.play(screen, events)
            if mode == "pause" or mode == "menu":
                esc_pressed = False
                clock.tick(g.FPS)
                pygame.display.flip()
                pygame.time.wait(100)
                continue

        if mode == "level2":
            g.LEVEL = "level2"
            mode = level2.play(screen, events)
            if mode == "pause" or mode == "menu":
                esc_pressed = False
                clock.tick(g.FPS)
                pygame.display.flip()
                pygame.time.wait(100)
                continue

        if mode == "explain":
            mode = explain.menu(screen, events)

        if mode == "pause":
            mode = pause.pause(screen, esc_pressed, events)

        if mode == "shop":
            mode = shop.shop(screen, events)


        # Update the display
        pygame.display.flip()
        # An die FPS anpassen
        clock.tick(g.FPS)
    # Pygame immer sauber beenden
    pygame.quit()


if __name__ == "__main__":
    main()
