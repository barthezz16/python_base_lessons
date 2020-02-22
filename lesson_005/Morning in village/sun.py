# -*- coding: utf-8 -*-
from random import random
# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 800)


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def sun(point):
    radius = 50
    sun_center = point
    sd.circle(center_position=sun_center, radius=radius, width=0)
    for angle in range(0, 361, 40):
        sd.vector(start=sun_center, angle=angle, length=120, width=3)


point = sd.get_point(100, 650)
sun(point=point)
