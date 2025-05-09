import pygame
import src.submodule.globals as g

background: pygame.Surface = None


def init_background() -> None:
    """
    Load the background-picture from the "assets/menu-background/city-background.png" path.
    """
    global background
    background = pygame.image.load("assets/menu-background/city-background.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))


def draw_button(screen: pygame.Surface, text: str, button: tuple[float, float, float, float], text_size, color: str) -> None:
    font = pygame.font.SysFont("Verdana", text_size)
    text = font.render(f"{text}", True, "black")
    # KI-Anfang
    # KI: ChatGPT
    # prompt: zentriere den Text abhängig vom Button
    text_rect = text.get_rect()
    text_rect.center = (int(button[0] + button[2] / 2), int(button[1] + button[3] / 2))
    # KI-Ende
    pygame.draw.rect(screen, color, button)
    screen.blit(text, text_rect)


def check_button_collide(screen: pygame.Surface, text: str, button: tuple[float, float, float, float], text_size, color: str) -> bool:
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]

    rect = pygame.Rect(button)
    true_or_false = rect.collidepoint(mouse_pos)
    if true_or_false:
        draw_button(screen, text, button, text_size, color)
        if click:
            return True
    return False




def draw_flip_happens(screen: pygame.Surface) -> None:
    """
    Draw the "Flip Happens" text on left side of the menu
    :param screen: pygame.Surface -> the Surface on which the text should be written
    :return None
    """
    # KI-Anfang
    # KI: ChatGPT
    # prompt: ich mache in pygame ein menü, das auf der linken seite Flip Happens hat
    # und die position ist abhängig von der grösse des Fensters, der text soll schön in der mitte des linken drittels
    # platziert sein. gebe mir die berechnung für die variablen size, x position und y position
    size = g.HEIGHT // 8
    font = pygame.font.SysFont("Impact", size, False, False)

    text_surface = font.render("FLIP HAPPENS!", False, 'white')
    text_surface = pygame.transform.rotate(text_surface, 90)

    text_width, text_height = text_surface.get_size()

    x = g.WIDTH // 6 - text_width // 2
    y = g.HEIGHT // 2 - text_height // 2
    # KI-Ende
    screen.blit(text_surface, (x, y))


def menu(screen: pygame.Surface) -> None:
    screen.blit(background, (0,0))
    draw_flip_happens(screen)

    exit_button = [g.WIDTH-g.WIDTH/50,0,g.WIDTH/50,g.WIDTH/50,g.HEIGHT//40]
    draw_button(screen, "X", (exit_button[0],exit_button[1],exit_button[2],exit_button[3]), exit_button[4], "grey")

    if check_button_collide(screen, "X",
                            (exit_button[0],exit_button[1],exit_button[2],exit_button[3]), exit_button[4], "red"):
        exit()


    return None