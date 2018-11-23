import pygame.font
from pygame.sprite import Sprite

class Button(Sprite):

    def __init__(self, settings, screen, msg, rect, color):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.button_color = color
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(rect[0],rect[1],rect[2],rect[3])

        self.prep_msg(msg)


    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

