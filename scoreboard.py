import pygame.font

class Scoreboard():
    """ Class for holding and displaying info about the score. """

    def __init__(self, ai_settings, screen, stats):
        """ Init of the score attributes. """

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settins = ai_settings
        self.stats = stats

        # Set the font for displaying the score info
        self.text_color = (90, 180, 240)
        self.font = pygame.font.SysFont(None, 48)

        # Prep of the initial score info
        self.prep_score()

    
    def prep_score(self):
        """ Display score in a generated image """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settins.bg_image)

        # Display the score in the top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """ Display score on the game screen """
        self.screen.blit(self.score_image, self.score_rect)