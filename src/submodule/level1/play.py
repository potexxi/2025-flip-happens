import pygame
import copy
import src.submodule.globals as g
import src.submodule.pause_menu.pause as pause
import src.submodule.level1.place_assets as assets
import src.submodule.skater.skater as player
from src.submodule.menu.menu import draw_button, check_button_collide

letters_collected: int = 0
coins_collected: int = 0
end: bool = False
win: bool = False


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
    assets.append_elements = True
    player.blocks = []
    player.halfpipes_left = []
    player.halfpipes_right = []
    player.high_ramps_left = []
    player.high_ramps_right = []
    player.fast_ramp = []
    player.poles = []

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


def save_stats(username) -> None:
    """
    Save the stats (coins, time...) of the player
    :param username: the username of the player
    """
    users = []
    # open the file and safe the entry in users
    with open("submodule/menu/ranked.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
    for line in content:
        lines_content = line.strip().split(";")
        users.append([lines_content[0], int(lines_content[1])])

    # clear the file
    with open("submodule/menu/ranked.txt", "w", encoding="utf-8") as file:
        file.write("")

    # Check if the user is already in the file and when not then append him
    append = True
    for entry in users:
        if username == entry[0]:
            append = False
            entry[1] += coins_collected
    if append:
        users.append([f'{username}', f'{coins_collected}'])
    # sort users:
    users = sort_users_by_score(users)
    # write the file
    for entry in users:
        with open("submodule/menu/ranked.txt", "a", encoding="utf-8") as file:
            file.write(f"{entry[0]};{entry[1]}\n")


def draw_coins_collected(screen: pygame.Surface, _coins_collected) -> None:
    """
    Draw the collected coins on the screen
    :param screen: pygame.Surface -> Where the coins shall be drawn
    :param _coins_collected: how many coins the player collected
    """
    font = pygame.font.Font("assets/fonts/LowresPixel-Regular.otf", g.HEIGHT//45)
    text = font.render(f"Coins: {_coins_collected}", False, (255, 215, 0))
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
    global win
    if (assets.time <= 0) or (letters_collected == 9 and assets.time > 0):
        picture = assets.you_won
        if assets.time <= 0:
            picture = assets.you_lost
        if letters_collected == 9 and assets.time > 0:
            win = True
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
        screen.blit(assets.background, (0, 0))
        # draw the level
        assets.draw_letters(screen, player_rect)
        assets.draw_assets(screen, player_rect)
        assets.time = assets.draw_clock(screen, assets.time)
        # draw the player
        player.draw(screen)
        # draw the fortschritt and collected coins
        pygame.draw.rect(screen, (59, 59, 59), (-10,-10,g.WIDTH//8.5,g.HEIGHT//15), border_radius=5)
        draw_coins_collected(screen, coins_collected)
        draw_letter_percentage(screen)
        # Move the player
        player.move()
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
            if win:
                save_stats(g.USERNAME)
            reset_stats()
            return "menu"

    return "level1"
