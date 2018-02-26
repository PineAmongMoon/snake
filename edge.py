# coding=utf-8
#
# 贪吃蛇
# 作者：俱源懋
#

import setting as st


class EdgeBace(st.Point, st.EdgeSetting):
    def __init__(self, local):
        super().__init__(self.color, local)


class Edge:
    def __init__(self):
        self.body = \
            [EdgeBace((x, -1)) for x in range(0, st.GameAreaSetting.width)] + \
            [EdgeBace((x, st.GameAreaSetting.hight)) for x in range(0, st.GameAreaSetting.width)] + \
            [EdgeBace((-1, y)) for y in range(0, st.GameAreaSetting.hight)] + \
            [EdgeBace((st.GameAreaSetting.width, y)) for y in range(0, st.GameAreaSetting.hight)] +\
            [
                EdgeBace((-1, -1)),
                EdgeBace((-1, st.GameAreaSetting.hight)),
                EdgeBace((st.GameAreaSetting.width, -1)),
                EdgeBace((st.GameAreaSetting.width, st.GameAreaSetting.hight)),
            ]

    def draw(self, surface):
        for item in self.body:
            item.draw(surface)
