import pygame
import random
import submodule.globals as g
import submodule.level1.play as play
import submodule.menu.menu as menu
import submodule.level1.place_assets as assets1
import submodule.level2.place_assets as assets2


screen_size: tuple[float, float] = (g.WIDTH//2, g.HEIGHT//2)
last_timestamp: int = 0
w_key: pygame.Surface = ...
a_key: pygame.Surface = ...
d_key: pygame.Surface = ...
s_key: pygame.Surface = ...
space_key: pygame.Surface = ...
esc_key: pygame.Surface = ...
ui_pause: pygame.Surface = ...
pause_button: tuple[float,float,float,float] = (g.WIDTH - g.WIDTH / 50 -5, 5, g.WIDTH / 50, g.WIDTH / 50)


def init() -> None:
    """
    Init the pictures , which are use for the pause-menu
    """
    global esc_key, a_key, d_key, w_key, s_key, space_key, ui_pause
    # Load the big images
    image_letters = pygame.image.load("assets/ui-controls/keys_letters.png")
    image_specials = pygame.image.load("assets/ui-controls/keys_special.png")
    # ESC:
    esc_key = image_specials.subsurface((30,0,30,16))
    esc_key = pygame.transform.scale(esc_key, (g.KEY_SIZE*1.5, g.KEY_SIZE))
    # Space:
    space_key = image_specials.subsurface((2 * 32.5, 2 * 16, 30, 16))
    space_key = pygame.transform.scale(space_key, (g.KEY_SIZE*2, g.KEY_SIZE))
    # W:
    w_key = image_letters.subsurface((6 * 16,4 * 16,16,16))
    w_key = pygame.transform.scale(w_key, (g.KEY_SIZE, g.KEY_SIZE))
    # S:
    s_key = image_letters.subsurface((2 * 16, 4 * 16, 16, 16))
    s_key = pygame.transform.scale(s_key, (g.KEY_SIZE, g.KEY_SIZE))
    # D:
    d_key = image_letters.subsurface((3 * 16, 2 * 16, 16, 16))
    d_key = pygame.transform.scale(d_key, (g.KEY_SIZE, g.KEY_SIZE))
    # A:
    a_key = image_letters.subsurface((0 * 16, 2 * 16, 16, 16))
    a_key = pygame.transform.scale(a_key, (g.KEY_SIZE, g.KEY_SIZE))
    # Pause Button:
    ui_pause = pygame.image.load("assets/ui-controls/menu.png").convert_alpha()
    ui_pause = pygame.transform.scale(ui_pause, (pause_button[2], pause_button[3]))


def draw(screen: pygame.Surface, events: list[pygame.event.Event]) -> str:
    """
    Draw the pause menu
    :param screen: pygame.Surface -> where the menu should be drawn
    :param events: the pressed keys of the player
    :return: str -> in which mode the games is in right now
    """
    # Buttons
    weiter_button = [g.WIDTH // 2 - (screen_size[0] / 2.5 ), g.HEIGHT / 2.2, screen_size[0] / 4,
                     screen_size[1] / 6, g.HEIGHT // 35]
    stop_button = [g.WIDTH // 2 - (screen_size[0] / 2.5 ),g.HEIGHT / 2.2 + (screen_size[0]/4 / 2),
                   screen_size[0] / 4, screen_size[1] / 6, g.HEIGHT // 35]

    pygame.draw.rect(screen, (20, 20, 60, 180), (g.WIDTH//2 - screen_size[0]//2,g.HEIGHT//2 - screen_size[1]//2
                                                     ,screen_size[0], screen_size[1]), border_radius=10)

    menu.draw_button(screen, "Weiter", (weiter_button[0], weiter_button[1], weiter_button[2], weiter_button[3]),
                weiter_button[4],  (211, 211, 211))
    menu.draw_button(screen, "Hauptmenü", (stop_button[0], stop_button[1], stop_button[2], stop_button[3]),
                stop_button[4], (211, 211, 211))

    if menu.check_button_collide(screen, "Weiter", (weiter_button[0], weiter_button[1], weiter_button[2]
                                            , weiter_button[3]), weiter_button[4] + 5, (255, 215, 0), events):
        return "play"
    if menu.check_button_collide(screen, "Hauptmenü", (stop_button[0], stop_button[1], stop_button[2]
                                            , stop_button[3]), stop_button[4] + 5, (255, 215, 0), events):
        play.reset_stats()
        return "menu"
    # Pause-Schrift
    font = pygame.font.Font("assets/fonts/ka1.ttf",g.HEIGHT//10)
    text = font.render("PAUSE", False, "white")
    text_width, text_height = text.get_size()
    screen.blit(text, (g.WIDTH // 2 - text_width // 2,g.HEIGHT//3.6))
    # Steuerung
    screen.blit(esc_key, (g.WIDTH//1.9,g.HEIGHT//2.2))
    screen.blit(w_key, (g.WIDTH // 1.7, g.HEIGHT // 2))
    screen.blit(a_key, (g.WIDTH // 1.8, g.HEIGHT // 1.8))
    screen.blit(s_key, (g.WIDTH // 1.7, g.HEIGHT // 1.8))
    screen.blit(d_key, (g.WIDTH // 1.6, g.HEIGHT // 1.8))
    screen.blit(space_key, (g.WIDTH // 1.6, g.HEIGHT // 1.6))
    font = pygame.font.Font("assets/fonts/normal.otf", g.HEIGHT//50)

    # A
    pygame.draw.line(screen, "white", (g.WIDTH//1.9, g.HEIGHT//1.6), (g.WIDTH//1.8, g.HEIGHT//1.7))
    text = font.render("nach links", False, "white")
    text_width, text_height = text.get_size()
    screen.blit(text, (g.WIDTH // 1.9 - text_width, g.HEIGHT // 1.6))

    # SPACE
    pygame.draw.line(screen, "white", (g.WIDTH // 1.7, g.HEIGHT // 1.45), (g.WIDTH // 1.6, g.HEIGHT // 1.5))
    text = font.render("Springen", False, "white")
    text_width, text_height = text.get_size()
    screen.blit(text, (g.WIDTH // 1.7 - text_width, g.HEIGHT // 1.45))

    # D
    pygame.draw.line(screen, "white", (g.WIDTH // 1.52, g.HEIGHT // 1.7), (g.WIDTH // 1.45, g.HEIGHT // 1.9))
    text = font.render("nach rechts", False, "white")
    text_width, text_height = text.get_size()
    screen.blit(text, (g.WIDTH // 1.45 - text_width//2, g.HEIGHT // 1.9 - text_height - 1))

    # ESC
    pygame.draw.line(screen, "white", (g.WIDTH // 1.75, g.HEIGHT // 2.1), (g.WIDTH // 1.7, g.HEIGHT // 2.15))
    text = font.render("Pause", False, "white")
    text_width, text_height = text.get_size()
    screen.blit(text, (g.WIDTH // 1.7 + 10, g.HEIGHT // 2.15 - text_height//2))

    return "pause"


def check_menu_button_pressed(screen: pygame.Surface, events: list[pygame.event.Event], pause: bool) -> bool:
    """
    Check if the user presses the menu-button
    :param screen: pygame.Surface -> where the icon should be drawn
    :param events: list of pygame events
    :param pause: if right now the player is in the pause menu
    :return: bool -> if the button gets pressed
    """
    if not pause:
        screen.blit(ui_pause, (pause_button[0], pause_button[1]))
    rect = pygame.Rect(pause_button)

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rect.collidepoint(pygame.mouse.get_pos()):
                menu.button_sound.play()
                return True
    return False


def pause(screen: pygame.Surface, esc: bool, events: list[pygame.event.Event]) -> str:
    """
    The pause-menu in the game
    :param screen: pygame.Surface -> where the menu should be drawn
    :param esc: True -> esc gets pressed -> false esc doesn't get pressed
    :param events: the keys the player pressed
    :return: the mode in which the game is right now (pause, start-menu, play...)
    """
    global last_timestamp
    # Draw the menu icon in time difference, so the icon doesn't get drawn too often
    timestamp = pygame.time.get_ticks()
    if timestamp - last_timestamp > 500:
        screen.blit(ui_pause, (pause_button[0], pause_button[1]))
    last_timestamp = timestamp

    # Draw the menu
    pause_screen: pygame.Surface = pygame.Surface((g.WIDTH, g.HEIGHT), pygame.SRCALPHA)
    mode = draw(pause_screen, events)
    if mode == "play":
        last_timestamp = 0
        return g.LEVEL
    elif mode == "menu":
        song_number = random.randint(1, 3)
        if song_number == 1: menu.menu_sound = menu.menu_sound1
        elif song_number == 2: menu.menu_sound = menu.menu_sound2
        elif song_number == 3: menu.menu_sound = menu.menu_sound3
        menu.menu_sound.play(fade_ms=5000)
        menu.change_phrase = True
        if g.LEVEL == "level1":
            assets1.music.fadeout(500)
        if g.LEVEL == "level2":
            assets2.music.fadeout(500)
        return "menu"
    screen.blit(pause_screen, (0, 0))

    # Check for button klicks pr esc
    if esc or check_menu_button_pressed(screen, events, True):
        last_timestamp = 0
        return g.LEVEL

    return "pause"
