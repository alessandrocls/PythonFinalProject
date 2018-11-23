import pygame as pg
from pygame.sprite import Sprite


class Player():

    def __init__(self, screen):
        super(Player, self).__init__()
        self.screen = screen
        new_width = 200
        new_height = 200
        self.image = pg.image.load('images/9454892_orig.png')
        self.image = pg.transform.scale(self.image, (new_width, new_height))
        # self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect = pg.Rect(200,200,200,200)

        # self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


