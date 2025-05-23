import pygame
import src.submodule.globals as g

original_logo: pygame.Surface = ...
logo_size: int = g.ASSETS_SIZE * 4

def init() -> None:
    global original_logo
    # Logo
    original_logo = pygame.image.load("assets/menu/logo.png")
    original_logo = pygame.transform.scale(original_logo, (g.ASSETS_SIZE*10, g.ASSETS_SIZE*10))


def animation(screen: pygame.Surface, _animation: bool) -> tuple[bool,str]:
    global logo_size, original_logo
    if _animation is True:
        logo_size += 2
        logo = pygame.transform.scale(original_logo, (logo_size, logo_size))
        screen.fill((0, 0, 0))
        logo_position: list[float] = [g.WIDTH // 2 - logo_size // 2, g.HEIGHT // 2 - logo_size // 2]
        screen.blit(logo, (logo_position[0], logo_position[1]))
        return logo_size < g.ASSETS_SIZE*10, "start"
    else:
        font = pygame.font.Font("assets/fonts/LowresPixel-Regular.otf", g.HEIGHT//40)
        text = font.render("Drücke [ENTER] für den Spielstart", True, (255,255,255))
        text = text.convert_alpha()
        text.set_alpha(1)
        text_width, text_height = text.get_size()
        screen.blit(text, (g.WIDTH//2 - text_width//2, g.HEIGHT//1.2))
        return False, "start"