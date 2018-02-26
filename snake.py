# coding=utf-8
#
# 贪吃蛇
# 作者：俱源懋
#

import setting as st


class SnakeBase(st.Point, st.SnakeSetting):
    def __init__(self, local):
        super().__init__(self.color, local)


class Snake(st.SnakeSetting):

    def __init__(self):
        self.forward = self.RIGHT
        self.body = [SnakeBase((i, st.GameAreaSetting.hight - 1)) for i in range(0, self.init_length)]

    def draw(self, surface):
        for item in self.body:
            item.draw(surface)

    def next_local(self):
        while True:
            local = 0, 0
            if self.forward == self.RIGHT:
                local = 1, 0
            elif self.forward == self.LEFT:
                local = -1, 0
            elif self.forward == self.UP:
                local = 0, -1
            elif self.forward == self.DOWN:
                local = 0, 1
            local = self.body[-1].local[0] + local[0], self.body[-1].local[1] + local[1]
            if local != self.body[-2].local:
                return local
            else:
                self.forward = self.forward ^ 0b11

    def move(self):
        self.body.pop(0)
        self.body.append(SnakeBase(self.next_local()))

    def grow(self):
        self.body.append(SnakeBase(self.next_local()))

    def is_dead(self):
        next_local = self.next_local()
        if next_local[0] < 0 or\
                next_local[0] >= st.GameAreaSetting.width or\
                next_local[1] < 0 or\
                next_local[1] >= st.GameAreaSetting.hight:
            return True
        if next_local in [item.local for item in self.body[1:]]:
            return True
        return False

    def is_get_apple(self, apple):
        return self.next_local() == apple.local
