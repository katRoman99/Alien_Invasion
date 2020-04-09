import sys

import pygame

from settings import Settings

def run_game():
    # Game init plus object creation
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption("Alien invasion")

    # Begin game's main loop
    while True:

        # Awaiting keyboard or mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)

        # Display last modified screen
        pygame.display.flip()

run_game()