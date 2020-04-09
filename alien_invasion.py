import sys

import pygame

def run_game():
    #Game init plus object creation
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien invasion")

    #Begin game's main loop
    while True:

        #Awaiting keyboard or mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Display last modified screen
        pygame.display.flip()

run_game()