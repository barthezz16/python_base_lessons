# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(300, 300)
# radius = 200
# # for _ in range(3):
# #     # radius += 20
# #     # sd.circle(center_position=point, radius=radius, width=2)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius)


# point = sd.get_point(300, 300)
# bubble(point=point, step=10)


# Нарисовать 10 пузырьков в ряд
# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 100)
#     bubble(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков
# for y in range(100, 301, 100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
def color_bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color)


for _ in range(100):
    point = sd.random_point()
    color_bubble(point=point, step=5, color=sd.random_color())

sd.pause()
