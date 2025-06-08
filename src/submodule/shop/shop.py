import pygame
import src.submodule.globals as g
import src.submodule.menu.menu as menu


weather_immun: pygame.Surface = ...
faster: pygame.Surface = ...
coins_multi: pygame.Surface = ...
icon_size: tuple[float, float] = (g.ASSETS_SIZE*2.5, g.ASSETS_SIZE*2.5)

def init() -> None:
    """
    Init all the pictures, that the shop needs
    """
    global weather_immun, faster, coins_multi
    # Icon of the weather immunity
    weather_immun = pygame.image.load("assets/shop/weather_immun.png").convert_alpha()
    weather_immun = pygame.transform.scale(weather_immun, icon_size)
    # Icon of faster
    faster = pygame.image.load("assets/shop/faster.png").convert_alpha()
    faster = pygame.transform.scale(faster, icon_size)
    # Coins Multiplier
    coins_multi = pygame.image.load("assets/shop/coins_multi.png").convert_alpha()
    coins_multi = pygame.transform.scale(coins_multi, icon_size)


def draw(screen: pygame.Surface) -> None:
    # Background:
    menu.move_background("start")
    background = pygame.image.load("assets/menu/blue_unsharp.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))
    screen.blit(background, g.POSITION_WORLD)
    screen.blit(background, (g.POSITION_WORLD[0] + screen.get_width(), g.POSITION_WORLD[1]))

    # Header
    font = pygame.font.Font("assets/fonts/Born2bSportyFS.otf", g.ASSETS_SIZE * 3)
    text = font.render("Shop", False, (211, 211, 211))
    text_width, text_height = text.get_size()
    screen.blit(text, (g.WIDTH//2 - text_width//2,0))

    # position of the icons
    icon_1 = (g.WIDTH // 4 - icon_size[0] // 2, g.HEIGHT // 2 - icon_size[1] // 2)
    icon_2 = (g.WIDTH // 2 - icon_size[0] // 2, g.HEIGHT // 2 - icon_size[1] // 2)
    icon_3 = (3 * g.WIDTH // 4 - icon_size[0] // 2, g.HEIGHT // 2 - icon_size[1] // 2)

    # Blit the background of the icons
    pygame.draw.rect(screen, (211, 211, 211), (icon_1[0]/1.043, icon_1[1]/1.035,
                                               g.ASSETS_SIZE*3, g.ASSETS_SIZE*3), border_radius=2)
    pygame.draw.rect(screen, (211, 211, 211), (icon_2[0] / 1.02, icon_2[1] / 1.035,
                                               g.ASSETS_SIZE * 3, g.ASSETS_SIZE * 3), border_radius=2)
    pygame.draw.rect(screen, (211, 211, 211), (icon_3[0] / 1.013, icon_3[1] / 1.035,
                                               g.ASSETS_SIZE * 3, g.ASSETS_SIZE * 3), border_radius=2)

    # Blit the icons
    screen.blit(faster, icon_1)
    screen.blit(coins_multi, icon_2)
    screen.blit(weather_immun, icon_3)

    # Buttons:
    # Exit
    menu.draw_button(screen, "Zurück", (g.WIDTH-g.WIDTH/17, 3 ,g.WIDTH/18, g.HEIGHT/35), 18,
                     (211,211,211))


def shop(screen: pygame.Surface) -> str:
    draw(screen)
    if menu.check_button_collide(screen, "Zurück", (g.WIDTH-g.WIDTH/17, 3 ,g.WIDTH/18, g.HEIGHT/35), 20,
                     (255, 215, 0)):
        return "menu"
    return "shop"