import pygame

class Settings():
    ''' Class that stores all settings realated to this game '''

    def __init__(self):
        ''' Init of game settings '''
        # Screen settings
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (120, 220, 255)
        self.bg_image = pygame.image.load('images/space_bg.bmp')

        # Ship and bullet settings
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 253, 182, 75

        self.bullets_allowed = 3
