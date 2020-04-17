class GameStats():
    """ Monitoring the game stats data """

    def __init__(self, ai_settings):
        """ Initialization of the statistics for this game """
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """ Initialization of the statistics than can change during the game """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1