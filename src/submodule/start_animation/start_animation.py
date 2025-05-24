import pygame
import math
import src.submodule.globals as g


original_logo: pygame.Surface = ...
logo_size: int = g.ASSETS_SIZE * 5


def init() -> None:
    """
    Init the logo.png for the animation
    """
    global original_logo
    # Logo
    original_logo = pygame.image.load("assets/menu/logo.png")
    original_logo = pygame.transform.scale(original_logo, (g.ASSETS_SIZE*10, g.ASSETS_SIZE*10))


def animation(screen: pygame.Surface, _animation: bool) -> tuple[bool,str]:
    """
    Animation for the game start
    :param screen: pygame.Surface -> where the animation shall be drawn
    :param _animation: if the animation is currently running
    :return: tuple[bool,str] bool: if the animation is still running, str: current game mode
    """
    global logo_size, original_logo
    if _animation is True:
        # Animation for the game start
        logo_size += 5
        logo = pygame.transform.scale(original_logo, (logo_size, logo_size))
        screen.fill((0, 0, 0))
        logo_position: list[float] = [g.WIDTH // 2 - logo_size // 2, g.HEIGHT // 2 - logo_size // 2]
        screen.blit(logo, (logo_position[0], logo_position[1]))
        return logo_size < g.ASSETS_SIZE*10, "start"
    else:
        font = pygame.font.Font("assets/fonts/LowresPixel-Regular.otf", g.HEIGHT//40)
        text = font.render("Drücke [ENTER] für den Spielstart", True, (255,255,255))
        screen.fill((0,0,0))
        logo = pygame.transform.scale(original_logo, (logo_size, logo_size))
        logo_position: list[float] = [g.WIDTH // 2 - logo_size // 2, g.HEIGHT // 2 - logo_size // 2]
        screen.blit(logo, (logo_position[0], logo_position[1]))
        text = text.convert_alpha()

        # KI-Anfang
        # KI: ChatGPT
        # prompt: wieso geht das nicht
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

        return False, "start"