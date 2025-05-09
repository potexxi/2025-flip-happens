from xml.sax.saxutils import prepare_input_source

import pygame
import src.submodule.globals as g

background: pygame.Surface = None
buttons: dict = {}
button_count: int = 0


def init_background() -> None:
    """
    Load the background-picture from the "assets/menu-background/city-background.png" path.
    """
    global background
    background = pygame.image.load("assets/menu-background/city-background.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))


def draw_button(screen: pygame.Surface, text: str, button: tuple[float, float, float, float]) -> None:
    global button_count
    button_count += 1

    font = pygame.font.SysFont("Verdana", 50)
    text = font.render(f"{text}", True, "black")

    pygame.draw.rect(screen, (200,200,200), button)
    screen.blit(text, (button[0], button[1]))


def draw_flip_happens(screen: pygame.Surface, size: int, position: tuple[float, float]) -> None:
    # KI-Anfang
    # KI: ChatGPT
    # prompt: ich mache in pygame ein menü, das auf der linken seite Flip Happens hat
    # und die position ist abhängig von der grösse des Fensters, der text soll schön in der mitte des linken drittels
    # platziert sein. gebe mir die berechnung für die variablen size, x position und y position
    size = g.HEIGHT // 8
    font = pygame.font.SysFont("Impact", size, False, False)

    text_surface = font.render("FLIP HAPPENS!", False, 'black')
    text_surface = pygame.transform.rotate(text_surface, 90)

    text_width, text_height = text_surface.get_size()

    x = g.WIDTH // 6 - text_width // 2
    y = g.HEIGHT // 2 - text_height // 2
    # KI-Ende
    screen.blit(text_surface, (x, y))


def menu(screen: pygame.Surface) -> None:
    screen.blit(background, (0,0))
    draw_flip_happens(screen, 100, (100, 500))
    draw_button(screen, "Hallo", (g.WIDTH/2-100,g.HEIGHT/3,g.WIDTH/10,g.HEIGHT/10)) # Todo: Buttons machen


    return None