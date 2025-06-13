import pygame
import submodule.globals as g
from submodule.menu.menu import draw_button, check_button_collide, move_background


def draw(screen: pygame.Surface, events: list[pygame.event.Event]) -> str:
    """
    Draw the explain-menu and Check all the button actions
    :param screen: pygame.Surface -> where the elements of the explain-menu shall be drawn
    :param events: the pressed keys of the player
    :return: current game mode, changes if the player presses the right button
    """
    # Background zeichnen
    background = pygame.image.load("assets/menu/blue_unsharp.png").convert_alpha()
    background = pygame.transform.scale(background, (g.WIDTH, g.HEIGHT))
    move_background("explain")
    screen.blit(background, g.POSITION_WORLD)
    screen.blit(background, (g.POSITION_WORLD[0] + screen.get_width(), g.POSITION_WORLD[1]))

    # Exit Button oben rechts
    exit_button = [g.WIDTH - g.WIDTH / 50, 0, g.WIDTH / 50, g.WIDTH / 50, g.HEIGHT // 40]
    draw_button(screen, "X", (exit_button[0], exit_button[1], exit_button[2], exit_button[3]),
                exit_button[4], (211, 211, 211))
    if check_button_collide(screen,
                            "X",
                            (exit_button[0],exit_button[1],exit_button[2],exit_button[3]), exit_button[4],
                            "red", events):
        exit("FLIP HAPPENS!")
    # KI-Start
    # KI: ChatGPT
    # prompt: surface_rect = (0,0,g.WIDTH/2, g.HEIGHT/2)
    #           mache den surface rect in die mitte des screens
    surface_x = (g.WIDTH - g.WIDTH // 1.2) // 2
    surface_y = (g.HEIGHT - g.HEIGHT // 1.2) // 2
    # KI-Ende
    # Menü Hintergrund
    pygame.draw.rect(screen, (200, 220, 255)
                     ,(surface_x, surface_y, g.WIDTH // 1.2, g.HEIGHT // 1.2), border_radius=10)
    back_button = (surface_x + g.WIDTH // 1.2 - g.WIDTH//14.2, surface_y , g.HEIGHT / 8, g.HEIGHT // 25)
    draw_button(screen, "Zurück", back_button, g.HEIGHT//45, "white")
    if check_button_collide(screen,"Zurück",back_button, g.HEIGHT//40, (255, 215, 0), events):
        return "menu"
    explain_text = [
        "1. Ziel  des  Spiels:", "   Meistere  das  Level  mit  deinem  Skater  –  so  schnell,  so  stylisch  wie  möglich!",
        "2. Level  abschließen:", "   Sammle  alle  Buchstaben  in  der  richtigen  Reihenfolge (alphabetisch),  um  die  Coins  auf  das  Konto  gutgeschrieben  zu  bekommen.",
        "3. Features  im  Level:", "   Bezwinge  Rampen,  grinde  Slides  und  nutze  jede  Chance  für  Tempo  und  Flow!",
        "4. Coins  sammeln:", "   Jeder  Coin  zählt  –  je  mehr  du  hast,  desto  höher  dein  Rang  in  der  Rangliste.",
        "5. Bestenliste:", "   Nur  die  mit  den  meisten  Coins  thronen  an  der  Spitze  der  Rangliste.",
        "6. Shop:", "   Tausch  Coins  gegen  Skill  –  doch  sei  bereit,  in  der  Rangliste  abzusteigen.",
        "7. Taktik  zählt:", "   Wähle  deinen  Weg:  Ewiger  Ruhm  oder  krasse  Extras  –  du  entscheidest!",
        "8. Steuerung:", "   Drücke  ESC,  um  in  das  Pausemenü  zu  finden,  in  dem  du  auch  die  Tastenbelegung  findest."
    ]
    font = pygame.font.Font("assets/fonts/normal.otf", g.HEIGHT // 45)
    counter = 0
    distance = g.HEIGHT // 20
    for idx, entry in enumerate(explain_text):
        if idx % 2 == 0:
            surface = font.render(entry, True, "black")
            counter += 1
        else:
            surface = font.render(entry, True, "black")
        surface_width, surface_height = surface.get_size()
        screen.blit(surface, (surface_x+g.WIDTH//100, surface_y +  idx * surface_height + counter * distance))
    return "explain"


def menu(screen: pygame.Surface, events: list[pygame.event.Event]) -> str:
    """
    Runs the explain-menu, the funktion which to call in the game loop
    :param screen: pygame.Surface -> where the explain-menu shall be drawn
    :param events: the pressed keys of the player
    :return: current gamemode, changes if the player presses the right button
    """
    surface_explain = pygame.Surface((g.WIDTH, g.HEIGHT), pygame.SRCALPHA).convert_alpha()
    mode = draw(surface_explain, events)
    screen.blit(surface_explain, (0,0))
    return mode