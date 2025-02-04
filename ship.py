import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen, ship_width, ship_height):
        ''' Init of the spaceship and its location on the screen '''
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        
        # Loading the ship image and its rect
        self.transform_ship(ship_width, ship_height)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Each new spaceship will show up in the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.bottom = self.screen_rect.bottom

        self.x_pos = float(self.rect.centerx)
        self.y_pos = float(self.rect.bottom)

        # Ship's moving right flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        ''' Update the position of the ship on the screen '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x_pos += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x_pos -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.y_pos -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y_pos += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.x_pos
        self.rect.bottom = self.y_pos

    def blitme(self):
        ''' Displaying the ship in a current location '''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.y_pos = float(self.rect.bottom)

    def transform_ship(self, width, height):
        """ Tranform ship image to smaller/ bigger size """
        self.image = pygame.transform.smoothscale(pygame.image.load('images/ship3.bmp'), (width, height))