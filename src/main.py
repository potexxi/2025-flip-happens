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

    mode = "start"

    esc_pressed = True
    esc_was_pressed = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    esc_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    esc_pressed = False

        if mode == "start":
            mode = start.animation(screen)

        if mode == "menu":
            mode = menu.menu(screen)

        if mode == "play":
            mode = level1.play(screen)

        if mode == "explain":
            mode = explain.menu(screen)

        # KI-Anfang
        # KI: ChatGPT
        # prompt: wie mache ich, dass esc_now nur dann True ist, wenn ich die Taste einmal drücke und nicht gedrückt
        # halte <der code ohne diese zeile>
        esc_now = esc_pressed and not esc_was_pressed
        # KI-Ende
        if mode == "pause":
            mode = pause.pause(screen, esc_now)
        esc_was_pressed = esc_pressed


        # Update the display
        pygame.display.flip()
        # An die FPS anpassen
        clock.tick(g.FPS)
    # Pygame immer sauber beenden
    pygame.quit()



if __name__ == "__main__":
    main()
