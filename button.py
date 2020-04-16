import pygame.font

class Button():
    """ Simple class representing a clickable button """

    def __init__(self, ai_settings, screen, msg):
        """ Initilization of the button """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Define size of the button and its attributes
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create the rect for this button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare the message for this button
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Generate a text to be centered on this button """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw an empty button and a message on it """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)