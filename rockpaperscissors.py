import sys
import pygame as pg
from config.settings import Settings
from config.player import Player
from config.enemy import Enemy
from config.buttons import Button
from config.probability import Probability
from config.game_stats import GameStats
import config.game_functions as gf
from pygame.sprite import Group



def run_game():

    pg.init()
    settings = Settings()
    screen = pg.display.set_mode((settings.screen_width,settings.screen_height))
    pg.display.set_caption("Magic RPS")
    player = Player(screen)
    enemy = Enemy(screen)
    stats = GameStats(settings)
    probability = Probability(settings,screen,stats)
    play_button = Button(settings,screen,"Play",[500,300,300,100],[230,30,30])
    rock = Button(settings,screen,"Rock",[150,450,400,100],(255,255,255))
    paper = Button(settings,screen,"Paper",[150,600,400,100],(255,255,255))
    scissors = Button(settings,screen,"Scissors",[700,450,400,100],(255,255,255))
    magic = Button(settings,screen,"Magic",[700,600,400,100],(85,120,255))
    while True:
        gf.check_events(rock,paper,scissors,magic,probability,settings,stats, play_button,enemy)
        gf.update_screen(settings,screen,player,rock,paper,scissors,magic,enemy,probability, play_button,stats)

run_game()