import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        ''' Init of the spaceship and its location on the screen '''
        self.ai_settings = ai_settings
        self.screen = screen
        
        # Loading the ship image and its rect
        self.image = pygame.transform.scale(pygame.image.load('images/ship.bmp'), (60, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Each new spaceship will show up at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # Ship's moving right flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        ''' Update the position of the ship on the screen '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        ''' Displaying the ship in a current location '''
        self.screen.blit(self.image, self.rect)