import pygame
import src.submodule.globals as g
import src.submodule.level1.place_blocks as draw_level
import src.submodule.pause_menu.pause as pause
import src.submodule.level1.place_assets as assets
import src.submodule.skater.skater as player

letters_collected: int = 9
coins_collected: int = 0
end: bool = False

def reset_stats() -> None:
    """
    Reset the stats of the player (coins, letters, time...)
    """
    global coins_collected, letters_collected
    assets.time = 120
    assets.coins_position = assets.coins_position_original.copy()
    player.x_position = 0
    player.y_position = 0
    player.last_direction = "right"
    coins_collected = 0
    letters_collected = 0


def draw_coins_collected(screen: pygame.Surface) -> None:
    """
    Draw the collected coins on the screen
    :param screen: pygame.Surface -> Where the coins shall be drawn
    """
    font = pygame.font.Font("assets/fonts/LowresPixel-Regular.otf", g.HEIGHT//45)
    text = font.render(f"Coins: {coins_collected}", False, (255, 215, 0))
    screen.blit(text, (5, g.HEIGHT//50 + 10))


def draw_letter_percentage(screen: pygame.Surface) -> None:
    """
    Draw a percentage beam, how many letters the player collected
    :param screen: pygame.Surface ->  where the beam shall be drawn
    """
    color_percentage = (231, 76, 60)
    rect_width = (g.WIDTH//13 / 9) * letters_collected
    percentage = (100/9) * letters_collected
    if 33 <= percentage <= 66:
        color_percentage = (255, 207, 51)
    elif percentage > 66:
        color_percentage = (63, 197, 107)
    pygame.draw.rect(screen,	(85, 85, 85), (5,5,g.WIDTH//13, g.HEIGHT//50), border_radius=5)
    pygame.draw.rect(screen, color_percentage, (5,5,rect_width, g.HEIGHT//50), border_radius=5)
    font = pygame.font.Font("assets/fonts/LowresPixel-Regular.otf", g.HEIGHT // 45)
    text = font.render(f"{percentage:.0f}%", False, (192, 192, 192))
    screen.blit(text, (g.WIDTH//13 + 10, 5))


def draw_lose(screen: pygame.Surface) -> None:
    pygame.draw.rect(screen, (85, 85, 85), (g.WIDTH//2 - (g.WIDTH//4),g.WIDTH//2, g.WIDTH//2))
    screen.blit(assets.you_lost, (0,0))


def draw_win(screen: pygame.Surface) -> None:
    screen.blit(assets.you_won, (0,0))



def check_for_win(screen: pygame.Surface) -> bool:
    if assets.time <= 0:
        draw_lose(screen)
        return True


    if letters_collected == 9 and assets.time > 0:
        draw_win(screen)
        return True
    return False


def play(screen: pygame.Surface, events: list[pygame.event.Event]) -> str:
    """
    Play level1
    :param screen: pygame.Surface -> where the game should be drawn
    :return: str -> in which mode the game is in
    """
    global end
    if end is False:
        player_rect = pygame.Rect((player.x_position, player.y_position, g.PLAYER_SIZE, g.PLAYER_SIZE))
        screen.blit(draw_level.background, (0, 0))
        player.move()
        draw_level.place_elements(screen)
        draw_level.place_bricks(screen)
        assets.draw_coins(screen, player_rect)
        assets.draw_letters(screen, player_rect)
        assets.draw_power_ups(screen)
        assets.draw_clock(screen)
        player.draw(screen)
        pygame.draw.rect(screen, (59, 59, 59), (-10,-10,g.WIDTH//8.5,g.HEIGHT//15), border_radius=5)
        draw_coins_collected(screen)
        draw_letter_percentage(screen)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "pause"
        if pause.check_menu_button_pressed(screen, events, False):
            return "pause"

    end = check_for_win(screen)


    return "play"
