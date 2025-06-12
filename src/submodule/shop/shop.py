import pygame
import submodule.globals as g
import submodule.menu.menu as menu
from submodule.level1.play import save_stats

weather_immun: pygame.Surface = ...
faster: pygame.Surface = ...
coins_multi: pygame.Surface = ...
icon_size: tuple[float, float] = (g.ASSETS_SIZE*2.5, g.ASSETS_SIZE*2.5)
price_coinsm: dict = {"1.2": 50, "1.4": 100, "1.6": 250, "1.8": 500, "2.0": 1000}
price_speed: dict = {"1.1": 25, "1.2": 50, "1.3": 150, "1.4": 350, "1.5": 750}


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
    # Background:
    menu.move_background("shop")
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
    font = pygame.font.Font("assets/fonts/normal.otf", int(g.ASSETS_SIZE/2.5))
    icon_text1 = font.render("Speed - Multiplikator", False, (211,211,211))
    icon_text2 = font.render("Coin - Multiplikator", False, (211, 211, 211))
    icon_text3 = font.render("Wetter Immunität", False, (211, 211, 211))
    screen.blit(icon_text1, (icon_1[0]/1.15, icon_1[1]/1.13))
    screen.blit(icon_text2, (icon_2[0] / 1.04, icon_2[1] / 1.13))
    screen.blit(icon_text3, (icon_3[0] / 1.02, icon_3[1] / 1.13))

    # User stats
    icon_text1 = font.render(f"Aktuell: {g.SPEEDM:.1f}x", False, (211,211,211))
    icon_text2 = font.render(f"Aktuell: {g.COINSM:.1f}x", False, (211,211,211))
    if g.IMMUNITY: icon_text3 = font.render("Aktuell: aktiv", False, (211,211,211))
    else: icon_text3 = font.render("Aktuell: inaktiv", False, (211,211,211))
    screen.blit(icon_text1, (icon_1[0] / 1.045, icon_1[1] / 0.7))
    screen.blit(icon_text2, (icon_2[0] / 1.018, icon_2[1] / 0.7))
    screen.blit(icon_text3, (icon_3[0] / 1.012, icon_3[1] / 0.7))

    # Price
    if g.SPEEDM < 1.45:
        icon_text1 = font.render(f"Preis: {price_speed[f"{g.SPEEDM + 0.1:.1f}"]} Coins", False, (255,215,0))
    if g.COINSM < 1.9:
        icon_text2 = font.render(f"Preis: {price_coinsm[f"{g.COINSM + 0.2:.1f}"]} Coins", False, (255,215,0))
    icon_text3 = font.render("Preis: 1000 Coins", False, (255, 215, 0))
    if g.SPEEDM < 1.45:
        screen.blit(icon_text1, (icon_1[0],icon_1[1]/0.58))
    if g.COINSM < 1.9:
        screen.blit(icon_text2, (icon_2[0],icon_2[1]/0.58))
    if not g.IMMUNITY:
        screen.blit(icon_text3, (icon_3[0],icon_3[1]/0.58))
    text = font.render(f"Coins: {g.COINS}", False, (255,215,0))
    screen.blit(text, (0,0))

    # Buttons:
    # Exit
    menu.draw_button(screen, "Zurück", (g.WIDTH-g.WIDTH/17, 3 ,g.WIDTH/18, g.HEIGHT/35), 18,
                     (211,211,211))

    # Button for the speed multiplier:
    if g.SPEEDM >= 1.45: text = "max."
    else: text = f"Kaufe {g.SPEEDM + 0.1:.1f}x"
    menu.draw_button(screen, text, (icon_1[0]//1.25, icon_1[1]//0.65, g.WIDTH//6, g.HEIGHT//15)
                     , g.HEIGHT//24, (211,211,211))
    if menu.check_button_collide(screen, text, (icon_1[0]//1.25, icon_1[1]//0.65, g.WIDTH//6, g.HEIGHT//15)
            , g.HEIGHT//22, (255, 215, 0)) and g.SPEEDM < 1.45 and g.COINS >= price_speed[f"{g.SPEEDM + 0.1:.1f}"]:
        pygame.time.wait(50)
        g.SPEEDM += 0.1
        save_stats(-price_speed[f"{g.SPEEDM:.1f}"])

    # Button for the coin multiplier:
    if g.COINSM >= 1.9: text = "max."
    else: text = f"Kaufe {g.COINSM + 0.2:.1f}x"
    menu.draw_button(screen, text, (icon_2[0]//1.1, icon_2[1]//0.65, g.WIDTH//6, g.HEIGHT//15)
                     , g.HEIGHT//24, (211,211,211))
    if menu.check_button_collide(screen, text, (icon_2[0]//1.1, icon_2[1]//0.65, g.WIDTH//6, g.HEIGHT//15)
            , g.HEIGHT//22, (255, 215, 0)) and g.COINSM < 1.9 and g.COINS >= price_coinsm[f"{g.COINSM + 0.2:.1f}"]:
        pygame.time.wait(50)
        g.COINSM += 0.2
        save_stats(-price_coinsm[f"{g.COINSM:.1f}"])

    # Button for the immunity:
    if g.IMMUNITY:
        text_size1 = g.HEIGHT//24
        text_size2 = g.HEIGHT//22
        text = "max."
    else:
        text = "Kaufe Wetter Immunität"
        text_size1 = g.HEIGHT//45
        text_size2 = g.HEIGHT//40
    menu.draw_button(screen, text, (icon_3[0]//1.05, icon_3[1]//0.65, g.WIDTH //6, g.HEIGHT // 15)
                     , text_size1, (211, 211, 211))
    if menu.check_button_collide(screen, text, (icon_3[0]//1.05, icon_3[1]//0.65, g.WIDTH // 6, g.HEIGHT // 15)
            , text_size2, (255, 215, 0)) and not g.IMMUNITY and g.COINS >= 1000:
        g.IMMUNITY = True
        save_stats(-1000)
        pygame.time.wait(50)


def shop(screen: pygame.Surface) -> str:
    """
    Draw the shop and check if the buttons get pressed
    :param screen: pygame.Surface -> where the shop shall be drawm
    :return: current game mode
    """
    draw(screen)
    # Check if the buttons get pressed
    if menu.check_button_collide(screen, "Zurück", (g.WIDTH-g.WIDTH/17, 3 ,g.WIDTH/18, g.HEIGHT/35), 20,
                     (255, 215, 0)):
        return "menu"
    return "shop"