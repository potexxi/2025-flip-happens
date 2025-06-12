import pygame
import math
import submodule.globals as g
from submodule.menu.menu import check_button_collide, draw_button, move_background, read_coins

original_logo: pygame.Surface = ...
background: pygame.Surface = ...
logo_size: int = g.ASSETS_SIZE * 5
ask_username: bool = False
wait_screen: bool = False
animation_: bool = True
button_activated: bool = False
text: str = ""


def init() -> None:
    """
    Init the logo.png for the animation
    """
    global original_logo, background
    # Logo
    original_logo = pygame.image.load("assets/menu/logo.png")
    original_logo = pygame.transform.scale(original_logo, (g.ASSETS_SIZE*10, g.ASSETS_SIZE*10))
    # Background
    background = pygame.image.load("assets/menu/blue_unsharp.png")
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))


def ask_for_username(screen: pygame.Surface, events: list[pygame.event.Event]) -> str:
    """
    Ask for the username
    :param screen: pygame.Surface -> where the menu shall be drawn
    :param events: the pressed keys of the player
    :return: current game mode
    """
    global button_activated, text
    for event in events:
        if event.type == pygame.KEYDOWN and button_activated:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_RETURN:
                button_activated = False
            elif event.key == pygame.K_ESCAPE or event.key == pygame.K_TAB or event.key == pygame.K_DELETE:
                pass
            elif len(text) < 15:
                text += event.unicode

    # background:
    move_background("start")
    screen.blit(background, g.POSITION_WORLD)
    screen.blit(background, (g.POSITION_WORLD[0] + screen.get_width(), g.POSITION_WORLD[1]))

    # warning
    font = pygame.font.Font("assets/fonts/normal.otf", g.HEIGHT//35)
    text_ = font.render(f"Der Username muss zwischen 3 und 15 Zeichen lang sein!", True, "white")
    text_width, text_height = text_.get_size()
    screen.blit(text_, (g.WIDTH//2 - text_width//2, g.HEIGHT - g.HEIGHT//1.2))


    # text button:
    text_button = (g.WIDTH//2 - g.WIDTH//4 / 2,g.HEIGHT//2 - g.HEIGHT//8 / 2, g.WIDTH//4, g.HEIGHT//8)
    button_color = 	(211, 211, 211)
    text_size = g.HEIGHT//35
    button_text = "Username"
    if button_activated:
        button_text = text
        text_size = g.HEIGHT//35 + 5
        button_color =	(255, 215, 0)
    if len(text) > 0:
        button_text = text

    # check if the player clicks ausserhalb of the button
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    rect = pygame.Rect(text_button)
    true_or_false = rect.collidepoint(mouse_pos)
    if not true_or_false and click:
        button_activated = False

    pygame.draw.rect(screen, button_color, text_button, border_radius=10)
    draw_button(screen, button_text, text_button, text_size, button_color)
    if check_button_collide(screen, button_text, text_button, text_size, (255, 215, 0)):
        button_activated = True

    # continue button
    continue_button = (g.WIDTH// 2 - g.WIDTH//6 / 2,g.HEIGHT - g.HEIGHT//3, g.WIDTH//6, g.HEIGHT//10)
    draw_button(screen, "Weiter", continue_button, g.HEIGHT//30, (211, 211, 211))
    if check_button_collide(screen, "Weiter", continue_button, g.HEIGHT//30 + 5, (255, 215, 0)):
        if 2 < len(text) < 16:
            g.USERNAME = text
            read_coins()
            pygame.time.wait(100)
            return "menu"
    return "start"


def animation(screen: pygame.Surface, events: list[pygame.event.Event]) -> str:
    """
    Animation for the game start
    :param screen: pygame.Surface -> where the animation shall be drawn
    :param events: pygame.event.Event -> the events the player pressed
    :return: current game mode
    """
    global logo_size, original_logo, ask_username, wait_screen, animation_
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_KP_ENTER] or pressed_keys[pygame.K_RETURN]:
        ask_username = True
        _animation = False
        wait_screen = False

    if animation_ is True:
        # Animation for the game start
        logo_size += 5
        logo = pygame.transform.scale(original_logo, (logo_size, logo_size))
        screen.fill((0, 0, 0))
        logo_position: list[float] = [g.WIDTH // 2 - logo_size // 2, g.HEIGHT // 2 - logo_size // 2]
        screen.blit(logo, (logo_position[0], logo_position[1]))
        if not(logo_size < g.ASSETS_SIZE*10):
            wait_screen = True
            animation_ = False

    if wait_screen is True:
        font = pygame.font.Font("assets/fonts/normal.otf", g.HEIGHT//40)
        text = font.render("Drücke [ENTER] für den Spielstart", True, (255,255,255))
        screen.fill((0,0,0))
        logo = pygame.transform.scale(original_logo, (logo_size, logo_size))
        logo_position: list[float] = [g.WIDTH // 2 - logo_size // 2, g.HEIGHT // 2 - logo_size // 2]
        screen.blit(logo, (logo_position[0], logo_position[1]))
        text = text.convert_alpha()

        # KI-Anfang
        # KI: ChatGPT
        # prompt: wieso geht das nicht:
        #         timestamp = pygame.time.get_ticks()
        #         up = False
        #         if timestamp-last_timestamp > 2000:
        #             up = not up
        #             counter += 1
        #             last_timestamp = counter * 2000
        #         print(up)
        #         if up is True:
        #             alpha += (255//2000)
        #         if up is False:
        #             alpha -= (255//2000)
        #         #print(alpha)
        #         text.set_alpha(alpha)
        time_ms = pygame.time.get_ticks()
        period = 2000  # Dauer einer vollen Ein-/Ausblende in ms
        alpha = int(127.5 * (math.sin(2 * math.pi * time_ms / period) + 1))
        # KI-Ende

        text.set_alpha(alpha)
        text_width, text_height = text.get_size()
        screen.blit(text, (g.WIDTH//2 - text_width//2, g.HEIGHT//1.2))

    if ask_username is True:
        return ask_for_username(screen, events)

    return "start"