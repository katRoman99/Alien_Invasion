import pygame

from pygame.sprite import Sprite
from pygame.rect import Rect

class Alien(Sprite):
    ''' Class representing a single alien in the alien fleet '''

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load an image of an alien
        self.image = pygame.transform.smoothscale(pygame.image.load('images/alien.bmp'), (90, 90))
        self.rect = Rect(self.image.get_rect().left, self.image.get_rect().top, 90, 50)

        # Place the newly created alien in the top corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the exact position of an alien
        self.x_pos = float(self.rect.x)


    def blitme(self):
        ''' Display an alien in its current location '''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        ''' Return true if an alien is on the edge of the screen '''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        ''' Move an alien to the right '''
        self.x_pos += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x_pos
