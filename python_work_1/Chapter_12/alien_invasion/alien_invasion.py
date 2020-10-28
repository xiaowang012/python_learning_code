import sys

import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf 


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("打外星人！！！")

    #设置屏幕背景颜色
    #bg_color=(200,150,200)

    #创建一个飞船
    ship=Ship(ai_settings,screen)

    #创建一个储存子弹的编组
    bullets=Group()

    #创建一个外星人
    alien=Alien(ai_settings,screen)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        #bullets.update()

        #删除已经消失在屏幕上的子弹，因为子弹并未消失，坐标为负，会继续消耗内存
       # for bullet in bullets.copy():
        #  if bullet.rect.bottom<=0:
         #   bullets.remove(bullet)
        #print(len(bullets))

        gf.update_screen(ai_settings,screen,ship,alien,bullets)

        #监听键盘和鼠标事件
        #for event in pygame.event.get():
          #  if event.type==pygame.QUIT:
          #      sys.exit()
        #每次循环都重新绘制屏幕
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()
        
        #让最近绘制的屏幕可见
        #pygame.display.flip()

run_game()
                

