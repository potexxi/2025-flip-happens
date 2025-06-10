import pygame
import src.submodule.globals as g
import src.submodule.menu.menu as menu


weather_immun: pygame.Surface = ...
faster: pygame.Surface = ...
coins_multi: pygame.Surface = ...
icon_size: tuple[float, float] = (g.ASSETS_SIZE*2.5, g.ASSETS_SIZE*2.5)
username = "test"
coins = 1000
coinsm = 1.4
speed = int(1.2)
immunity = False

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
    """
    Draw the shop on the screen
    :param screen: pygame.Surface -> where the shop shall be drawm
    """
    global speed
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

    # Icon Beschriftung
    font = pygame.font.Font("assets/fonts/normal.otf", g.ASSETS_SIZE//3)
    icon_text1 = font.render("Speed - Multiplikator", False, (211,211,211))
    icon_text2 = font.render("Coin - Multiplikator", False, (211, 211, 211))
    icon_text3 = font.render("Wetter Immunität", False, (211, 211, 211))
    screen.blit(icon_text1, (icon_1[0]/1.065, icon_1[1]/1.13))
    screen.blit(icon_text2, (icon_2[0] / 1.018, icon_2[1] / 1.13))
    screen.blit(icon_text3, (icon_3[0] / 1.007, icon_3[1] / 1.13))

    # User stats
    icon_text1 = font.render(f"Aktuell: {speed}x", False, (211,211,211))
    icon_text2 = font.render(f"Aktuell: {coinsm}x", False, (211,211,211))
    if immunity: icon_text3 = font.render("Wetter Immunität: aktiv", False, (211,211,211))
    else: icon_text3 = font.render("Wetter Immunität: inaktiv", False, (211,211,211))
    screen.blit(icon_text1, (icon_1[0] / 1.045, icon_1[1] / 0.7))
    screen.blit(icon_text2, (icon_2[0] / 1.018, icon_2[1] / 0.7))
    screen.blit(icon_text3, (icon_3[0] / 1.012, icon_3[1] / 0.7))

    # Buttons:
    # Exit
    menu.draw_button(screen, "Zurück", (g.WIDTH-g.WIDTH/17, 3 ,g.WIDTH/18, g.HEIGHT/35), 18,
                     (211,211,211))
    # Button1:
    if speed >= 2: text = "max."
    else:
        speed += 0.2
        text = f"{speed}"
    #menu.draw_button(screen, text, icon_1, 40)




def shop(screen: pygame.Surface) -> str:
    """
    Draw the shop and check if the buttons get pressed
    :param screen: pygame.Surface -> where the shop shall be drawm
    :return: current game mode
    """
    draw(screen)
    if menu.check_button_collide(screen, "Zurück", (g.WIDTH-g.WIDTH/17, 3 ,g.WIDTH/18, g.HEIGHT/35), 20,
                     (255, 215, 0)):
        return "menu"
    return "shop"