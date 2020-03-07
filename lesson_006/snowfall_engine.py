# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 800)

x_list = []
y_list = []
y_list0 = []
snowflake_size = []


def snowflake_creating(snowflake_count):
    global x_list, y_list, snowflake_size
    x_list = []
    y_list = []
    snowflake_size = []
    for i in range(snowflake_count):
        x_list.append(sd.random_number(25, 1000))
        y_list.append(sd.random_number(100, 780))
        snowflake_size.append(sd.random_number(15, 35))


def snowflake_color(snowflake_count, color=sd.COLOR_WHITE):
    snowflake_creating(25)
    global x_list, y_list
    for i, y in enumerate(y_list):
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.background_color)
        move_snowflake(3, 5)
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.COLOR_WHITE)


def snowflake_deleting():
    #  Здесь цикл по снежинкам, проверка 'y' координаты, добавление этой координаты в новый список
    #  Обновлять координату не нужно
    for i in y_list:
        if i < 20:
            y_list0.append(i)
    # if y_list[i] < 10:
    #     y_list[i] = 800
    # return y_list[i]


def move_snowflake(x_position=3, y_position=5):
    # TODO Здесь цикл по снежинкам, с изменением координат (42, 43 строка)
    # TODO создание точек, snowflake_deleting и sd.snowflake - удалить
    for i, y in enumerate(y_list):
        x_list[i] -= sd.random_number(-x_position, x_position)
        y_list[i] -= y_position
        point = sd.get_point(x_list[i], y_list[i])

snowflake_color(25)


sd.pause()
