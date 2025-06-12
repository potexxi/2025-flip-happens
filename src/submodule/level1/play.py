import random
import pygame
import copy
import src.submodule.globals as g
import src.submodule.pause_menu.pause as pause
import src.submodule.level1.place_assets as assets
import src.submodule.skater.skater as player
from src.submodule.menu.menu import draw_button, check_button_collide
from src.submodule.rain.rain import rain
import src.submodule.level2.place_assets as assets2
import src.submodule.level2.play as play2

letters_collected: int = 0
coins_collected: int = 0
end: bool = False
begin: bool = True
rain_bool: bool = False


def reset_stats() -> None:
    """
    Reset the stats of the player (coins, letters, time...)
    """
    global coins_collected, letters_collected, rain_bool, begin
    if g.LEVEL == "level1":
        assets.time = 120
        assets.collectables = copy.deepcopy(assets.collectables_original)
        assets.collectables.reverse()
        coins_collected = 0
        letters_collected = 0
        assets.append_elements = True
        rain_bool = False
        begin = True
    if g.LEVEL == "level2":
        assets2.time = 180
        assets2.assets = copy.deepcopy(assets2.assets_original)
        assets2.assets.reverse()
        play2.coins_collected = 0
        play2.letters_collected = 0
        play2.rain_bool = False
        play2.begin = True
        assets2.append_elements = True
    assets.next_letter_idx = 0
    player.x_position = 0
    player.y_position = g.HEIGHT - 2 * g.PLAYER_SIZE
    player.last_direction = "right"
    player.blocks = []
    player.halfpipes_left = []
    player.halfpipes_right = []
    player.high_ramps_left = []
    player.high_ramps_right = []
    player.fast_ramp = []
    player.poles = []
    rain_bool = False
    begin = True

# KI-Anfang:
# KI: ChatGPT
# prompt:programmiere mir eine sortier funktion, dass ich eine liste mit users sortieren kann, die liste ist wie folgt aufgebaut:
# ['EXAMPLE1', '1000']
# ['EXAMPLE2', '1000000']
# ['EXAMPLE3', '100000']
# ['EXAMPLE4', '10000']
# ['EXAMPLE5', '1040']
# ['EXAMPLE6', '14000040']
#
# sortiere nach dem zweiten eintrag der listen in der liste
def sort_users_by_score(users: list[list[str]]) -> list[list[str]]:
    """
    Sort the users list from the score of the users
    :param users: the list with all users and their coins
    :return: the sorted list
    """
    return sorted(users, key=lambda x: int(x[1]), reverse=True)
# KI-Ende


def save_stats(_coins_collected: int) -> None:
    """
    Save the stats (coins, time...) of the player in the right .txt file
    :param _coins_collected: how many coins the player collected
    """
    users = []
    # open the file and safe the entry in users
    with open("submodule/menu/ranked.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
    for line in content:
        lines_content = line.strip().split(";")
        users.append([lines_content[0], int(lines_content[1]), float(lines_content[2]), float(lines_content[3]),
                      lines_content[4]])

    # clear the file
    with open("submodule/menu/ranked.txt", "w", encoding="utf-8") as file:
        file.write("")

    # Check if the user is already in the file and when not then append him
    append = True
    for entry in users:
        if g.USERNAME == entry[0]:
            append = False
            entry[1] += _coins_collected
            g.COINS += _coins_collected
            entry[2] = float(f"{g.SPEEDM:.1f}")
            entry[3] = float(f"{g.COINSM:.1f}")
            entry[4] = str(g.IMMUNITY)
    if append:
        users.append([f'{g.USERNAME}', int(g.COINS + _coins_collected), float(g.SPEEDM), float(g.COINSM), str(g.IMMUNITY)])
        g.COINS += _coins_collected
    # sort users:
    users = sort_users_by_score(users)
    # write the file
    for entry in users:
        with open("submodule/menu/ranked.txt", "a", encoding="utf-8") as file:
            file.write(f"{entry[0]};{entry[1]};{entry[2]};{entry[3]};{entry[4]}\n")


def draw_coins_collected(screen: pygame.Surface, _coins_collected: int) -> None:
    """
    Draw the cointer of the collected coins on the screen
    :param screen: pygame.Surface -> where the coins shall be drawn
    :param _coins_collected: how many coins the player collected
    """
    font = pygame.font.Font("assets/fonts/normal.otf", g.HEIGHT//45)
    text = font.render(f"Coins: {_coins_collected}", False, (255, 215, 0))
    screen.blit(text, (5, g.HEIGHT//50 + 10))


def draw_letter_percentage(screen: pygame.Surface, _letters_collected: int) -> None:
    """
    Draw a percentage beam, how many letters the player collected
    :param screen: pygame.Surface ->  where the beam shall be drawn
    :param _letters_collected: how many letters the player collected
    """
    color_percentage = (231, 76, 60)
    rect_width = (g.WIDTH//13 / 9) * _letters_collected
    percentage = (100/9) * _letters_collected
    if 33 <= percentage <= 66:
        color_percentage = (255, 207, 51)
    elif percentage > 66:
        color_percentage = (63, 197, 107)
    pygame.draw.rect(screen,	(85, 85, 85), (5,5,g.WIDTH//13, g.HEIGHT//50), border_radius=5)
    pygame.draw.rect(screen, color_percentage, (5,5,rect_width, g.HEIGHT//50), border_radius=5)
    font = pygame.font.Font("assets/fonts/normal.otf", g.HEIGHT // 45)
    text = font.render(f"{percentage:.0f}%", False, (192, 192, 192))
    screen.blit(text, (g.WIDTH//13 + 10, 5))


def check_for_win_lose(screen: pygame.Surface, time, _letters_collected: int) -> tuple[bool, bool]:
    """
    Check if the player won/lost the game and draw it
    :param screen: pygame.Surface -> where the pictures shall be drawn
    :param time: how much time is left
    :param _letters_collected: how many letters the player already collected
    :return: 1. bool -> if the game is over, 2.bool -> if the player won
    """
    win = False
    if (time <= 0) or (_letters_collected == 9 and time > 0):
        picture = assets.you_won
        if time <= 0:
            picture = assets.you_lost
        if _letters_collected == 9 and assets.time > 0:
            win = True
            picture = assets.you_won
        pygame.draw.rect(screen, (85, 85, 85),
                         (g.WIDTH // 2 - (g.WIDTH // 4), g.HEIGHT // 2 - (g.WIDTH//3) / 2, g.WIDTH // 2, g.WIDTH // 3),
                         border_radius=5)
        picture_width, picture_height = picture.get_size()
        screen.blit(picture, (g.WIDTH//2 - picture_width//2, g.HEIGHT//7))
        return True, win
    return False, win


def play(screen: pygame.Surface, events: list[pygame.event.Event]) -> str:
    """
    Funktion to call in game loop, contains all the button checks and blit all the stuff to blit
    :param screen: pygame.Surface -> where the game should be drawn
    :param events: the keys the player pressed
    :return: str -> in which mode the game is in
    """
    global end, rain_bool, begin
    if begin:
        if random.random() < 0.4:
            rain_bool = True
    if end is False:
        player_rect = pygame.Rect((player.x_position, player.y_position, g.PLAYER_SIZE, g.PLAYER_SIZE))
        # background
        screen.blit(assets.background, (0, 0))
        # draw the level
        assets.draw_letters(screen, player_rect, assets.letters_position)
        assets.draw_assets(screen, player_rect)
        assets.time = assets.draw_clock(screen, assets.time)
        # draw the fortschritt and collected coins
        pygame.draw.rect(screen, (59, 59, 59), (-10,-10,g.WIDTH//8.5,g.HEIGHT//15), border_radius=5)
        draw_coins_collected(screen, coins_collected)
        draw_letter_percentage(screen, letters_collected)
        # Move the player
        player.move(rain_bool)
        # draw the player
        player.draw(screen)
        # Change, that begin is False
        begin = False
        # Rain:
        if rain_bool:
            rain(screen)
        # check for esc pressing or button pressing
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "pause"
        if pause.check_menu_button_pressed(screen, events, False):
            return "pause"
    end, win = check_for_win_lose(screen, assets.time, letters_collected)
    if end:
        button = [g.WIDTH // 2 - (g.WIDTH / 8)//2, g.HEIGHT / 1.5,
                       g.WIDTH / 8, g.HEIGHT / 12, g.HEIGHT // 35]
        draw_button(screen, "Hauptmenü",
                    (button[0], button[1], button[2], button[3]), button[4], (211, 211, 211))
        if check_button_collide(screen, "Hauptmenü",
                             (button[0], button[1], button[2], button[3]), button[4]+5, (255, 215, 0)):
            if win:
                save_stats(int(f"{coins_collected * g.COINSM:.0f}"))
            reset_stats()
            return "menu"

    return "level1"
