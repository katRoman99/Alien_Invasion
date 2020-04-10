import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Game init plus object creation
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
    pygame.display.set_caption("Alien invasion")

    ship = Ship(screen)

    # Begin game's main loop
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()