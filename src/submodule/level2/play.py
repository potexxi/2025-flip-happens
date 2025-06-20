import pygame
import random
import submodule.level1.play as level1
import submodule.globals as g
import submodule.level2.place_assets as assets2
import submodule.skater.skater as player
from submodule.rain.rain import rain
import submodule.level1.place_assets as assets1
import submodule.menu.menu as menu
import submodule.pause_menu.pause as pause

coins_collected: int = 0
rain_bool: bool = False
begin: bool = True
letters_collected: int = 0
end: bool = False


def play(screen: pygame.Surface, events: list[pygame.event.Event]) -> str:
    """
    Funktion to call in the game loop, contains all the button checks and blit all the assets stuff
    :param screen: pygame.Surface -> where the level2 shall be drawn
    :param events: the keys the player pressed
    :return: the current game mode
    """
    global rain_bool, end, begin
    if begin:
        assets2.music.play(fade_ms=500)
        if random.random() < 0.4:
            rain_bool = True
    if end is False:
        player_rect = pygame.Rect((player.x_position, player.y_position, g.PLAYER_SIZE, g.PLAYER_SIZE))
        assets2.draw_assets(screen, player_rect)
        # draw letters
        pygame.draw.rect(screen, (59, 59, 59), (-10, -10, g.WIDTH // 8.5, g.HEIGHT // 15), border_radius=5)
        assets1.draw_letters(screen, player_rect, assets2.letters_position)
        level1.draw_letter_percentage(screen, letters_collected)
        level1.draw_coins_collected(screen, coins_collected)
        # Move the player
        player.move(rain_bool)
        # Player:
        player.draw(screen)
        # Change, that begin isn't now
        begin = False
        # Rain:
        if rain_bool:
            rain(screen)
        # Check if the player presses the esc key
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "pause"
        # check if the player presses the menu button
        if pause.check_menu_button_pressed(screen, events, False):
            return "pause"
    end, win = level1.check_for_win_lose(screen, assets2.time, letters_collected)
    if end:
        button = [g.WIDTH // 2 - (g.WIDTH / 8) // 2, g.HEIGHT / 1.5,
                  g.WIDTH / 8, g.HEIGHT / 12, g.HEIGHT // 35]
        menu.draw_button(screen, "Hauptmenü",
                    (button[0], button[1], button[2], button[3]), button[4], (211, 211, 211))
        if menu.check_button_collide(screen, "Hauptmenü",
                                (button[0], button[1], button[2], button[3]), button[4] + 5, (255, 215, 0), events):
            song_number = random.randint(1, 3)
            if song_number == 1:
                menu.menu_sound = menu.menu_sound1
            elif song_number == 2:
                menu.menu_sound = menu.menu_sound2
            elif song_number == 3:
                menu.menu_sound = menu.menu_sound3
            menu.menu_sound.play(fade_ms=5000)
            menu.change_phrase = True
            assets2.music.fadeout(500)
            if win:
                level1.save_stats(int(f"{coins_collected * g.COINSM:.0f}"))
            level1.reset_stats()
            return "menu"

    return "level2"