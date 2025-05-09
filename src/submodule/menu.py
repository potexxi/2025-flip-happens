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


def menu(screen: pygame.Surface) -> None:
    screen.blit(background, (0,0))
    draw_button(screen, "Hallo", (g.WIDTH/2-100,g.HEIGHT/3,g.WIDTH/10,g.HEIGHT/10))


    return None