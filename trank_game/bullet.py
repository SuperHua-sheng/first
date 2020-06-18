import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,trank):
        super(Bullet,self).__init__()
        self.screen=screen
        #在（0，0）绘制表示子弹的矩形
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #设置正确位置，覆盖前面数据
        self.rect.centerx=trank.rect.centerx
        self.rect.top=trank.rect.top
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
    def update(self):
        #更新子弹位置
        self.y-=self.speed_factor
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)