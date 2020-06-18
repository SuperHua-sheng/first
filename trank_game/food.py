import pygame
from pygame.sprite import Sprite
class Food(Sprite):
    def __init__(self,ai_settings,screen):
        super(Food,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #加载图像，设置rect值
        self.image=pygame.image.load('food.bmp')
        self.rect=self.image.get_rect()
        #设置外星人初始位置
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def check(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
    def update(self):
        #右移动
        self.x+=(self.ai_settings.food_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x=self.x