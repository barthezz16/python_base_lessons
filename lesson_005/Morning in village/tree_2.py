# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)



def branch(point, angle, length):
    if length < 1:
        return
    if 1 < length < 10:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v1.draw(color=sd.COLOR_DARK_GREEN)
    else:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v1.draw(color=sd.COLOR_DARK_ORANGE)
        next_length = length * .75
        angle_1 = angle + 30
        angle_2 = angle - 30
        branch(point=v1.end_point, angle=angle_1, length=next_length)
        branch(point=v1.end_point, angle=angle_2, length=next_length)


point_0 = sd.get_point(900, 0)
angle_0 = 90
length = 50

if __name__ == '__main__':
    branch(point=point_0, angle=angle_0, length=length)
