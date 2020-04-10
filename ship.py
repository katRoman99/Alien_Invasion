import pygame

class Ship():

    def __init__(self, screen):
        ''' Init of the spaceship and its location on the screen '''
        self.screen = screen
        
        # Loading the ship image and its rect
        self.image = pygame.transform.scale(pygame.image.load('images/ship.bmp'), (65, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Each new spaceship will show up at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        ''' Displaying the ship in a current location '''
        self.screen.blit(self.image, self.rect)