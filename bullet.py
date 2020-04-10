import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' Class that manages bullets fired by a ship '''

    def __init__(self, ai_settings, screen, ship):
        ''' Create the bullet object in the current ship position '''
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect((0, 0), ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y_pos = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        ''' Steers the bullet on the screen '''
        self.y_pos -= self.speed_factor
        self.rect.y = self.y_pos

    def draw_bullet(self):
        ''' Draws a bullet on the screen '''
        pygame.draw.rect(self.screen, self.color, self.rect)