import sys
from time import sleep
import random
import pygame as pg


def check_events(rock,paper,scissors,magic,probability,settings,stats,play_button,enemy):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            check_button_click(rock,paper,scissors,magic,mouse_x,mouse_y,probability,settings, stats, play_button,enemy)

def check_button_click(rock,paper,scissors,magic,mouse_x,mouse_y,probability,settings,stats, play_button,enemy):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        settings.initialize_dynamic_settings()
        probability.rock = 1
        probability.scissors = 1
        probability.paper = 1
        probability.prep_probability()
        probability.prep_score()
        stats.reset_stats()
        stats.game_active = True
    rock_button_clicked = rock.rect.collidepoint(mouse_x, mouse_y)
    paper_button_clicked = paper.rect.collidepoint(mouse_x,mouse_y)
    scissors_button_clicked = scissors.rect.collidepoint(mouse_x,mouse_y)
    magic_button_clicked = magic.rect.collidepoint(mouse_x,mouse_y)
    if rock_button_clicked:
        combat(settings,"r",probability,stats,enemy)
    elif paper_button_clicked:
        combat(settings,"p",probability,stats,enemy)
    elif scissors_button_clicked:
        combat(settings,"s",probability,stats,enemy)
    elif magic_button_clicked:
        settings.count += 1
        if settings.count < 3:
            probability_list = probability_alter()
            if probability_list[0] == "r":
                probability.rock += probability_list[1]
                probability.prep_probability()
            elif probability_list[0] == "p":
                probability.paper += probability_list[1]
                probability.prep_probability()
            elif probability_list[0] == "s":
                probability.scissors += probability_list[1]
                probability.prep_probability()

def combat(settings, move, probability,stats,enemy):
    sum = probability.rock + probability.paper + probability.scissors
    enemy_move = random.randint(1,sum)
    if enemy_move <= probability.rock and move == "p":
        print("win")
        pg.mixer.music.load('sounds/victory.mp3')
        pg.mixer.music.play(0)
        probability.stats.score += 1
        settings.count = 0
        probability_list = probability_alter()
        if probability_list[0] == "r":
            probability.rock += probability_list[1]
            probability.prep_probability()
        elif probability_list[0] == "p":
            probability.paper += probability_list[1]
            probability.prep_probability()
        elif probability_list[0] == "s":
            probability.scissors += probability_list[1]
            probability.prep_probability()
        probability.prep_score()
        enemy.blitme()
    elif enemy_move <= probability.rock and move == "s":
        pg.mixer.music.load('sounds/lost.mp3')
        pg.mixer.music.play(0)
        stats.game_active = False
    elif probability.rock < enemy_move < (sum-probability.scissors) and move == "s":
        print("win")
        pg.mixer.music.load('sounds/victory.mp3')
        pg.mixer.music.play(0)
        settings.count = 0
        probability.stats.score += 1
        settings.count = 0
        probability_list = probability_alter()
        if probability_list[0] == "r":
            probability.rock += probability_list[1]
            probability.prep_probability()
        elif probability_list[0] == "p":
            probability.paper += probability_list[1]
            probability.prep_probability()
        elif probability_list[0] == "s":
            probability.scissors += probability_list[1]
            probability.prep_probability()
        probability.prep_score()
        enemy.blitme()
    elif probability.rock < enemy_move < (sum-probability.scissors) and move == "r":
        pg.mixer.music.load('sounds/lost.mp3')
        pg.mixer.music.play(0)
        stats.game_active = False
    elif probability.rock + probability.paper < enemy_move and move == "r":
        pg.mixer.music.load('sounds/lost.mp3')
        pg.mixer.music.play(0)
        stats.game_active = False
    elif probability.rock + probability.paper < enemy_move and move == "p":
        print("win")
        pg.mixer.music.load('sounds/victory.mp3')
        pg.mixer.music.play(0)
        settings.increase_level()
        settings.count = 0
        probability.stats.score += 1
        settings.count = 0
        probability_list = probability_alter()
        if probability_list[0] == "r":
            probability.rock += probability_list[1]
            probability.prep_probability()
        elif probability_list[0] == "p":
            probability.paper += probability_list[1]
            probability.prep_probability()
        elif probability_list[0] == "s":
            probability.scissors += probability_list[1]
            probability.prep_probability()

        probability.prep_score()
        enemy.random(enemy.list)
        enemy.blitme()
    elif enemy_move <= probability.rock and move == 'r':
        pg.mixer.music.load('sounds/draw.mp3')
        pg.mixer.music.play(0)
    elif probability.rock < enemy_move < (sum-probability.scissors) and move == 'p':
        pg.mixer.music.load('sounds/draw.mp3')
        pg.mixer.music.play(0)
    elif probability.rock + probability.paper < enemy_move and move == 's':
        pg.mixer.music.load('sounds/draw.mp3')
        pg.mixer.music.play(0)

def probability_alter():
    list = ["r", "p", "s"]
    index = random.randint(0, len(list)-1)
    num = random.randint(1, 5)
    # print(list[index],num)
    return [list[index], num]


def update_screen(settings, screen, player,rock,paper,scissors, magic, enemy,probability, play_button, stats):
    screen.fill(settings.bg_color)

    if stats.game_active:
        player.blitme()
        enemy.blitme()
        rock.draw_button()
        paper.draw_button()
        scissors.draw_button()
        magic.draw_button()
        probability.show_probability()
    else:
        play_button.draw_button()
    pg.display.flip()
