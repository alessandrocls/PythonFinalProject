import pygame as pg
from pygame.sprite import Sprite
import random


class Enemy():

    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.list = ["4Head.png","Jebaited.png","WutFace.png","haHAA.jpg"]
        self.index = self.random(self.list)
        self.screen = screen
        self.new_width = 200
        self.new_height = 200
        self.image = pg.image.load('images/{}'.format(self.list[self.index]))
        self.image = pg.transform.scale(self.image, (self.new_width, self.new_height))
        # self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect = pg.Rect(900,200,100,100)

        # self.rect.centery = self.screen_rect.centery
        # self.rect.left = self.screen_rect.left
        self.center = float(self.rect.centerx)

    def random(self, list):
        return random.randint(0,len(list)-1)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


