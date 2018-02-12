# coding=utf-8
#
# 贪吃蛇
# 作者：俱源懋
#
# 游戏设置
#

import pygame


class PointSetting:
    length = 6
    size = length, length


class Point(PointSetting):
    def __init__(self, color, local):
        self.local = local
        self.color = color
        self.rect = pygame.Rect(coordinate_transform(local), self.size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


def coordinate_transform(local):
    return (local[0] + 1) * PointSetting.length, (local[1] + 1) * PointSetting.length


class GameAreaSetting:
    color = 0x66, 0xcc, 0xff
    width = 100
    hight = 100


class WindowSetting:
    game_tetle = "贪吃蛇"
    width = (GameAreaSetting.width + 2) * PointSetting.length
    hight = (GameAreaSetting.hight + 2) * PointSetting.length
    size = width, hight


class EdgeSetting:
    color = 0, 0, 0


class SnakeSetting:
    color = 0, 0xff, 0
    init_length = 10

    RIGHT = 0b00
    LEFT = 0b11
    UP = 0b01
    DOWN = 0b10


class AppleSetting:
    color = 0xff, 0, 0
