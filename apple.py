# coding=utf-8
#
# 贪吃蛇
# 作者：俱源懋
#


import setting as st


class Apple(st.Point, st.AppleSetting):
    def __init__(self, local):
        super().__init__(self.color, local)
