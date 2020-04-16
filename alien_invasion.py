import pygame

from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
import game_functions as gf

def run_game():
    # Game init plus object creation
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Game")
    
    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Begin game's main loop
    while True:
        gf.check_events(ai_settings, screen, stats, ship, aliens, bullets, play_button)

        # Check if the game is still running
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()