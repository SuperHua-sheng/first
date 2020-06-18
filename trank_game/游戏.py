import pygame
import game_function as gf
from settings import Settings
from trank import Trank
from pygame.sprite import Group
from food import Food
def run_game():
    pygame.init()#创建一个游戏窗口
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    trank = Trank(ai_settings, screen)
    food=Food(ai_settings,screen)
    bullets=Group()
    foods=Group()
    #创建群
    gf.create_fleet(ai_settings,screen,foods)
    #创建游戏循环
    while True:
        gf.check_events(ai_settings,screen,trank,bullets)
        trank.update()
        gf.update_bullets(foods,bullets)
        gf.update_foods(ai_settings,foods)
        gf.update_screen(ai_settings,screen,trank,foods,bullets)

run_game()