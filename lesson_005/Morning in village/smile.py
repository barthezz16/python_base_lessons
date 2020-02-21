# -*- coding: utf-8 -*-
from random import random
# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 800)
# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(point):
    radius = 50
    circle_center = point  # Теперь точку можно задавать извне :)
    mouth_x_start = circle_center.x - 20
    mouth_y_start = circle_center.y - 20
    mouth_start = sd.get_point(mouth_x_start, mouth_y_start)
    mouth_x_end = circle_center.x + 20
    mouth_y_end = circle_center.y - 20
    mouth_end = sd.get_point(mouth_x_end, mouth_y_end)
    sd.line(start_point=mouth_start, end_point=mouth_end)
    sd.circle(center_position=circle_center, radius=radius)
    left_eye_x = circle_center.x - 20
    left_eye_y = circle_center.y + 13
    left_eye = sd.get_point(left_eye_x, left_eye_y)
    sd.circle(center_position=left_eye, radius=10)
    right_eye_x = circle_center.x + 20
    right_eye_y = circle_center.y + 13
    right_eye = sd.get_point(right_eye_x, right_eye_y)
    sd.circle(center_position=right_eye, radius=10)



point = sd.get_point(500, 100)
smile(point=point)



#зачет!