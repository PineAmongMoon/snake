# coding=utf-8
#
# 贪吃蛇
# 作者：俱源懋
#
# 程序入口
#

import sys

import random

import time

import pygame

import setting as st

import snake

import edge

import apple

pygame.init()
screen = pygame.display.set_mode(st.WindowSetting.size)
pygame.display.set_caption(st.WindowSetting().game_tetle)
my_snake = snake.Snake()
my_edge = edge.Edge()
my_apple = apple.Apple((st.GameAreaSetting.width//2, st.GameAreaSetting.hight//2))

while True:

    """游戏主循环"""

    begin_time = time.clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                my_snake.forward = my_snake.RIGHT
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                my_snake.forward = my_snake.LEFT
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                my_snake.forward = my_snake.UP
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                my_snake.forward = my_snake.DOWN

    if my_snake.is_dead():
        sys.exit()

    if my_snake.is_get_apple(my_apple):
        my_snake.grow()

        while True:
            local = random.randint(0,st.GameAreaSetting.width-1), random.randint(0,st.GameAreaSetting.hight-1)
            flg = True
            for item in my_snake.body:
                if local == item.local:
                    flg = False
                    break
            if flg:
               break
        my_apple = apple.Apple(local)

    else:
        my_snake.move()

    screen.fill(st.GameAreaSetting.color)
    my_edge.draw(screen)
    my_apple.draw(screen)
    my_snake.draw(screen)
    pygame.display.flip()

    time.sleep(max(0, 0.125-time.clock()+begin_time))
