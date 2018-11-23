import pygame as pg

class Probability:
    def __init__(self,settings,screen,stats):
        self.settings = settings
        self.rock = self.settings.difficulty
        self.paper = self.settings.difficulty
        self.scissors = self.settings.difficulty
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.text_color = (30,30,30)
        self.font = pg.font.SysFont(None, 48)

        self.prep_probability()
        self.prep_score()

    def prep_probability(self):
        self.rock_image = self.font.render("Rock: {}".format(self.rock), True, self.text_color, self.settings.bg_color)
        self.paper_image = self.font.render("Paper: {}".format(self.paper), True, self.text_color, self.settings.bg_color)
        self.scissors_image = self.font.render("Scissors: {}".format(self.scissors), True, self.text_color, self.settings.bg_color)

        self.rock_rect = self.rock_image.get_rect()
        self.paper_rect = self.rock_image.get_rect()
        self.scissors_rect = self.rock_image.get_rect()

        self.rock_rect.right = self.screen_rect.right - 100
        self.paper_rect.right = self.rock_rect.right
        self.scissors_rect.right = self.rock_rect.right

        self.rock_rect.top = self.screen_rect.top + 50
        self.paper_rect.top = self.rock_rect.bottom
        self.scissors_rect.top = self.paper_rect.bottom

    def prep_score(self):
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.rock_rect.right -500
        self.score_rect.top = self.rock_rect.top

    def show_probability(self):
        self.screen.blit(self.rock_image, self.rock_rect)
        self.screen.blit(self.paper_image, self.paper_rect)
        self.screen.blit(self.scissors_image, self.scissors_rect)
        self.screen.blit(self.score_image,self.score_rect)