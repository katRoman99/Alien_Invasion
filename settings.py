import pygame

class Settings():
    ''' Class that stores all settings realated to this game '''

    def __init__(self):
        ''' Init of game settings '''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (120, 220, 255)
        self.bg_image = pygame.image.load('images/space_bg.bmp')

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 253, 182, 75

        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.ship_limit = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Init of the game's dynamic properties """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2.5
        self.alien_speed_factor = 1
        # Direction 1 = right , -1 = left
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """ Change the properties connected with speed """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)