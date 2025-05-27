import pygame
import copy
import src.submodule.globals as g
import src.submodule.level1.place_blocks as draw_level
import src.submodule.pause_menu.pause as pause
import src.submodule.level1.place_assets as assets
import src.submodule.skater.skater as player
from src.submodule.menu.menu import draw_button, check_button_collide

letters_collected: int = 0
coins_collected: int = 0
end: bool = False


def reset_stats() -> None:
    """
    Reset the stats of the player (coins, letters, time...)
    """
    global coins_collected, letters_collected
    assets.time = 120
    assets.collectables = copy.deepcopy(assets.collectables_original)
    assets.collectables.reverse()
    player.x_position = 0
    player.y_position = g.HEIGHT - 2 * g.PLAYER_SIZE
    player.last_direction = "right"
    coins_collected = 0
    letters_collected = 0
    assets.next_letter_idx = 0


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


def check_for_win_lose(screen: pygame.Surface) -> bool:
    """
    Check if the player won/lost the game and draw it
    :param screen: pygame.Surface -> where the pictures shall be drawn
    :return: True -> the player lost/won, False -> the game continues
    """
    if (assets.time <= 0) or (letters_collected == 9 and assets.time > 0):
        picture = assets.you_won
        if assets.time <= 0:
            picture = assets.you_lost
        if letters_collected == 9 and assets.time > 0:
            picture = assets.you_won
        pygame.draw.rect(screen, (85, 85, 85),
                         (g.WIDTH // 2 - (g.WIDTH // 4), g.HEIGHT // 2 - (g.WIDTH//3) / 2, g.WIDTH // 2, g.WIDTH // 3),
                         border_radius=5)
        picture_width, picture_height = picture.get_size()
        screen.blit(picture, (g.WIDTH//2 - picture_width//2, g.HEIGHT//7))
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
        # background
        screen.blit(draw_level.background, (0, 0))
        # Move the player
        player.move()
        # draw the level and place blocks, poles...
        draw_level.place_elements(screen)
        draw_level.place_bricks(screen)
        # draw the collectables
        assets.draw_letters(screen, player_rect)
        assets.draw_collectables(screen, player_rect)
        assets.draw_clock(screen)
        # draw the player
        player.draw(screen)
        # draw the fortschritt and collected coins
        pygame.draw.rect(screen, (59, 59, 59), (-10,-10,g.WIDTH//8.5,g.HEIGHT//15), border_radius=5)
        draw_coins_collected(screen)
        draw_letter_percentage(screen)
        # check for esc pressing or button pressing
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "pause"
        if pause.check_menu_button_pressed(screen, events, False):
            return "pause"
    end = check_for_win_lose(screen)
    if end:
        button = [g.WIDTH // 2 - (g.WIDTH / 8)//2, g.HEIGHT / 1.5,
                       g.WIDTH / 8, g.HEIGHT / 12, g.HEIGHT // 35]
        draw_button(screen, "Hauptmenü",
                    (button[0], button[1], button[2], button[3]), button[4], (211, 211, 211))
        if check_button_collide(screen, "Hauptmenü",
                             (button[0], button[1], button[2], button[3]), button[4]+5, (255, 215, 0)):
            reset_stats()
            return "menu"

    return "play"
