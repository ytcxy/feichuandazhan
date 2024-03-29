import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并且获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘飞创放在屏幕底部中央
        # print(self.rect.center, self.rect.bottom)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # print(self.rect.centerx, self.rect.bottom)
        self.center = float(self.rect.centerx)
        self.bott = float(self.rect.bottom)
        # 移动状态
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # 根据移动标志调整飞船的位置
        # 更新飞船的 centter 值，而不是 rect 值。
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bott += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.bottom > 0:
            self.bott -= self.ai_settings.ship_speed_factor
        self.rect.bottom = self.bott
        self.rect.centerx = self.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.bott = self.screen_rect.bottom
