import pygame

class Trank():
    def __init__(self,ai_settings,screen):
        #初始化坦克并设置初始位置
        self.screen=screen
        self.ai_settings=ai_settings

        #加载图片获取外接矩形
        self.image=pygame.image.load('trank.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将坦克放在屏幕底部中央(centerx表示X轴，bottom表示Y轴)
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)

        #移动标志
        self.moving_right=False
        self.moving_left=False
        self.moving_down=False
        self.moving_up=False


    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.trank_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.trank_speed_factor
        if self.moving_down and self.rect.bottom<=self.screen_rect.bottom:
            self.rect.bottom += 2
        if self.moving_up and self.rect.top>0:
            self.rect.bottom -= 2

        self.rect.centerx=self.center


    def blitme(self):
        #指定位置绘制坦克
        self.screen.blit(self.image,self.rect)
