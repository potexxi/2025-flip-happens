import pygame
import sys
import submodule.globals as g

background: pygame.Surface = ...
ask_for_level_: bool = False


def init() -> None:
    """
    Load the background-picture from the "assets/menu/city-background.png" path.
    """
    global background
    background = pygame.image.load("assets/menu/blue_unsharp.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))


def read_coins() -> None:
    """
    Read the coins of the user if he played before
    """
    with open(g.save, "r", encoding='utf-8') as file:
        content = file.readlines()
    for line in content:
        entrys = line.strip().split(';')
        if entrys[0] == g.USERNAME:
            g.COINS = int(entrys[1])
            g.SPEEDM = float(entrys[2])
            g.COINSM = float(entrys[3])
            if entrys[4] == 'False':
                g.IMMUNITY = False
            else:
                g.IMMUNITY = True


def draw_button(screen: pygame.Surface, text: str, button: tuple[float, float, float, float],
                text_size: int, color: int or str) -> None:
    """
    Draw a button
    :param screen: pygame.Surface -> where the button should be drawn
    :param text: text, which is on the button
    :param button:  with all the information about the button(x_position, y_position, width and height)
    :param text_size: the size of the text on the button
    :param color: the color of the button
    :return: None
    """
    font = pygame.font.Font("assets/fonts/normal.otf", text_size)
    text = font.render(f"{text}", True, "black")
    # KI-Anfang
    # KI: ChatGPT
    # prompt: zentriere den Text abhängig vom Button
    text_rect = text.get_rect()
    text_rect.center = (int(button[0] + button[2] / 2), int(button[1] + button[3] / 2))
    # KI-Ende
    pygame.draw.rect(screen, color, button, border_radius=10)
    screen.blit(text, text_rect)


def check_button_collide(screen: pygame.Surface, text: str, button: tuple[float, float, float, float],
                         text_size: int, color: int or str) -> bool:
    """
    Check if the player clicks on a button or just hovers it.
    :param screen: pygame.Surface -> where the new button (different color) should be drawn
    :param text: text, which is on the new button (different color)
    :param button:  with all the information about the new button(x_position, y_position, width and height)(different color)
    :param text_size: the size of the text on the new button (different color)
    :param color: the color of the new button (different color)
    :return: True, if the button gets clicked. False, if the button only gets hovered
    """
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]

    rect = pygame.Rect(button)
    true_or_false = rect.collidepoint(mouse_pos)
    if true_or_false:
        draw_button(screen, text, button, text_size, color)
        if click:
            if text == "START":
                pygame.time.wait(100)
            else:
                pygame.time.wait(20)
            return True
    return False


def draw_flip_happens(screen: pygame.Surface) -> None:
    """
    Draw the "Flip Happens" text on left side of the menu
    :param screen: pygame.Surface -> the Surface on which the text should be written
    """
    # KI-Anfang
    # KI: ChatGPT
    # prompt: ich mache in pygame ein menü, das auf der linken seite Flip Happens hat
    # und die position ist abhängig von der grösse des Fensters, der text soll schön in der mitte des linken drittels
    # platziert sein. gebe mir die berechnung für die variablen size, x position und y position
    size = g.HEIGHT // 6
    font = pygame.font.Font("assets/fonts/Born2bSportyFS.otf", size)

    text_surface = font.render("FLIP HAPPENS!", True, 'white')
    text_surface = pygame.transform.rotate(text_surface, 90)

    text_width, text_height = text_surface.get_size()

    x = g.WIDTH // 6 - text_width // 2
    y = g.HEIGHT // 2 - text_height // 2
    # KI-Ende
    screen.blit(text_surface, (x, y))


def draw_ranked(screen: pygame.Surface) -> None:
    """
    Draw the ranked-list in the downer-right corner of the pygame.Surface
    :param screen: pygame.Surface -> where the list shall be drawn
    """
    # Read the list from the .txt file

    box_rect = [g.WIDTH - g.WIDTH / 6 + 10, g.HEIGHT - g.HEIGHT / 5 + 10, g.WIDTH / 6, g.HEIGHT / 5, g.HEIGHT // 100]
    box_surface = pygame.Surface((box_rect[2], box_rect[3]), pygame.SRCALPHA)
    pygame.draw.rect(box_surface, (0, 0, 139, 100), (0, 0, box_rect[2], box_rect[3]), border_radius=15)
    screen.blit(box_surface, (box_rect[0], box_rect[1]))

    font_top = pygame.font.Font("assets/fonts/normal.otf", box_rect[4]+g.HEIGHT//100)
    font_down = pygame.font.Font("assets/fonts/normal.otf", box_rect[4]+g.HEIGHT//140)
    msg1 = font_top.render("FLIP-HAPPENS Bestenliste", True, (255, 215, 0))
    screen.blit(msg1, (box_rect[0] + 10, box_rect[1] + 5))
    with open(g.save, "r",encoding="utf-8") as file:
        content = file.readlines()
    counter = 1
    for line in content:
        if counter > 6:
            msg2 = font_down.render(". . .", True, (255, 215, 0))
            text_width, text_height = msg2.get_size()
            screen.blit(msg2, ((box_rect[0] + 10), (box_rect[1] + 5) + (counter * (text_height + g.HEIGHT / 200)
                                                                        + g.HEIGHT // 100)))
            return None
        line = line.strip()
        line_content = line.split(";")
        msg2 = font_down.render(f"{counter}. {line_content[0]}: {line_content[1]}", True, (255, 215, 0))
        text_width, text_height = msg2.get_size()
        screen.blit(msg2, ((box_rect[0] + 10), (box_rect[1] + 5) + (counter * (text_height + g.HEIGHT / 200)
                                                                    + g.HEIGHT//100)))
        counter += 1
    return None


def move_background(menu_type: str) -> None:
    """
    Move the background x-pixel to the left
    :param menu_type: current game mode
    """
    if menu_type == "explain":
        speed = 1.3
    elif menu_type == "start":
        speed = 0.5
    elif menu_type == "shop":
        speed = 1.1
    else:
        speed = 0.3
    g.POSITION_WORLD[0] -= speed
    if g.POSITION_WORLD[0] < -g.WIDTH:
        g.POSITION_WORLD[0] = 0


def ask_for_level(screen: pygame.Surface) -> str:
    """
    Ask the player which level wants to play
    :param screen: pygame.Surface -> where the buttons shall be drawn
    :return: the current game mode
    """
    global ask_for_level_
    level1_button = (g.WIDTH / 2 - g.WIDTH/5 /2, g.HEIGHT / 2 - g.HEIGHT/10, g.WIDTH/5, g.HEIGHT/10)
    level2_button = (g.WIDTH / 2 - g.WIDTH/5 /2, g.HEIGHT / 2 + g.HEIGHT/10, g.WIDTH/5, g.HEIGHT/10)

    draw_button(screen, "Level 1", level1_button, g.HEIGHT//50, (211, 211, 211))
    draw_button(screen, "Level 2", level2_button, g.HEIGHT//50, (211, 211, 211))

    if check_button_collide(screen,"Level 1", level1_button, g.HEIGHT//50 + 5, (255, 215, 0)):
        ask_for_level_ = False
        return "level1"
    if check_button_collide(screen,"Level 2", level2_button, g.HEIGHT//50 + 5, (255, 215, 0)):
        ask_for_level_ = False
        return "level2"
    return "menu"


def menu(screen: pygame.Surface) -> str:
    """
    Blit the menu and check button collides-> in the game: select between PLAY, ERKLÄRUNG or STOP
    :param screen: pygame.Surface -> the Surface where the menu shall be drawn
    :return: str -> current game mode
    """
    global ask_for_level_
    # Move the background and blit it
    move_background("menu")
    screen.blit(background, g.POSITION_WORLD)
    screen.blit(background, (g.POSITION_WORLD[0] + screen.get_width(), g.POSITION_WORLD[1]))

    if ask_for_level_:
        return ask_for_level(screen)

    # ranked list
    draw_flip_happens(screen)

    # Username and Coins:
    font = pygame.font.Font("assets/fonts/normal.otf", g.HEIGHT//50)
    text = font.render(f"Username: {g.USERNAME}", False, (255,215,0))
    text_width, text_height = text.get_size()
    screen.blit(text, (5,0))
    text = font.render(f"Coins: {g.COINS}", False, (255,215,0))
    screen.blit(text, (5, text_height * 1.5))

    # KI-Anfang
    # KI: ChatGPT
    # prompt: gebe mir die Positionen und Größen von folgenden Buttons: exit_button (ganz oben rechts), start_button
    # (in der Mitte eher oben), explain_button (unter start button), stop_button (unter explain button)
    exit_button = [g.WIDTH - g.WIDTH / 50, 0, g.WIDTH / 50, g.WIDTH / 50, g.HEIGHT // 35]
    start_button = [g.WIDTH / 2 - g.WIDTH / 12 / 2, g.HEIGHT / 3, g.WIDTH / 8, g.HEIGHT / 12, g.HEIGHT // 35]
    explain_button = [g.WIDTH / 2 - g.WIDTH / 12 / 2, g.HEIGHT / 3 + g.HEIGHT / 15 + g.HEIGHT / 20, g.WIDTH / 8,
                      g.HEIGHT / 12, g.HEIGHT // 35]
    stop_button = [g.WIDTH / 2 - g.WIDTH / 12 / 2, g.HEIGHT / 3 + 2 * (g.HEIGHT / 15 + g.HEIGHT / 20), g.WIDTH / 8,
                   g.HEIGHT / 12, g.HEIGHT // 35]
    # KI-Ende

    # Draw the buttons
    draw_button(screen, "X", (exit_button[0],exit_button[1],exit_button[2],exit_button[3]),
                exit_button[4], (211, 211, 211))

    draw_button(screen, "START", (start_button[0],start_button[1],start_button[2],start_button[3]), g.HEIGHT // 40,
                (211, 211, 211))

    draw_button(screen, "SHOP", (stop_button[0], stop_button[1], stop_button[2], stop_button[3]), g.HEIGHT // 40,
                (211, 211, 211))

    draw_button(screen, "ERKLÄRUNG", (explain_button[0], explain_button[1], explain_button[2], explain_button[3])
                , g.HEIGHT // 40,	(211, 211, 211))

    # Draw the ranked list
    draw_ranked(screen)

    # Check for button collision:
    if check_button_collide(screen,
                            "X",
                            (exit_button[0],exit_button[1],exit_button[2],exit_button[3]), exit_button[4],
                            "red"):
        pygame.quit()
        sys.exit()

    if check_button_collide(screen,
                            "START",
                            (start_button[0], start_button[1], start_button[2], start_button[3]), start_button[4],
                            (255, 215, 0)):
        ask_for_level_ = True

    if check_button_collide(screen,
                            "ERKLÄRUNG",
                            (explain_button[0], explain_button[1], explain_button[2], explain_button[3]), explain_button[4],
                            (255, 215, 0)):
        return "explain"

    if check_button_collide(screen,
                            "SHOP",
                            (stop_button[0], stop_button[1], stop_button[2], stop_button[3]),stop_button[4],
                            (255, 215, 0)):
        return "shop"
    return "menu"