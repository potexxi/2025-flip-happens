import pygame
import src.submodule.level1.place_blocks as draw_level
import src.submodule.pause_menu.pause as pause
import src.submodule.level1.place_assets as assets
import src.submodule.skater.skater as player



def play(screen: pygame.Surface, events: list[pygame.event.Event]) -> str:
    """
    Play level1
    :param screen: pygame.Surface -> where the game should be drawn
    :return: str -> in which mode the game is in
    """
    screen.blit(draw_level.background, (0, 0))
    player.move()
    draw_level.place_elements(screen)
    draw_level.place_bricks(screen)
    assets.draw_coins(screen)
    assets.draw_letters(screen)
    assets.draw_power_ups(screen)
    assets.draw_clock(screen)
    player.draw(screen)

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "pause"

    if pause.check_menu_button_pressed(screen, events, False):
        return "pause"

    return "play"
