import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Game init plus object creation
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
    pygame.display.set_caption("Alien invasion")

    ship = Ship(screen)

    # Begin game's main loop
    while True:

        # Awaiting keyboard or mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Display last modified screen
        pygame.display.flip()

run_game()