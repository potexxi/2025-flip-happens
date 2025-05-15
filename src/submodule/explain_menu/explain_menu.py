import pygame
import src.submodule.globals as g
from src.submodule.menu.menu import draw_button, check_button_collide


def draw(screen: pygame.Surface) -> None:
    exit_button = [g.WIDTH - g.WIDTH / 50, 0, g.WIDTH / 50, g.WIDTH / 50, g.HEIGHT // 40]
    draw_button(screen, "X", (exit_button[0], exit_button[1], exit_button[2], exit_button[3]),
                exit_button[4], (211, 211, 211))
    if check_button_collide(screen,
                            "X",
                            (exit_button[0],exit_button[1],exit_button[2],exit_button[3]), exit_button[4],
                            "red"):
        exit("FLIP HAPPENS!")
    # KI-Start
    # KI: ChatGPT
    # prompt: surface_rect = (0,0,g.WIDTH/2, g.HEIGHT/2)
    #           mache den surface rect in die mitte des screens
    surface_x = (g.WIDTH - g.WIDTH // 1.2) // 2
    surface_y = (g.HEIGHT - g.HEIGHT // 1.2) // 2
    # KI-Ende
    pygame.draw.rect(screen, (200, 220, 255, 230)
                     ,(surface_x, surface_y, g.WIDTH // 1.2, g.HEIGHT // 1.2), border_radius=15)


def menu(screen: pygame.Surface) -> str:
    surface_explain = pygame.Surface((g.WIDTH, g.HEIGHT), pygame.SRCALPHA).convert_alpha()
    draw(surface_explain)
    screen.blit(surface_explain, (0,0))
    return "explain"