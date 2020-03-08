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


def snowflake_color(snowflake_count, color=sd.COLOR_WHITE):  # TODO Параметр snowflake_count удаляем
    snowflake_creating(25)  # TODO Эту строку удаляем
    global x_list, y_list
    for i, y in enumerate(y_list):
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.background_color)  # TODO Эту строку удаляем
        move_snowflake(3, 5)  # TODO Эту строку удаляем
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.COLOR_WHITE)  # TODO А тут вместо sd.color_white
        # TODO используем параметр функции color


def snowflake_deleting():
    #  Здесь цикл по снежинкам, проверка 'y' координаты, добавление этой координаты в новый список
    #  Обновлять координату не нужно
    for i in y_list:  # TODO Изменения в правильную сторону, однако
        # TODO 1) До цикла нужно создавать список index_list пусть будет
        # TODO 2) В сам список нужно вносить не координату из y_list, а индекс этой координаты в списке
        # TODO Поэтому тут тоже используем for i, y in enumerate(y_list):
        # TODO При этом 'y' проверяем, а 'i' добавляем в index_list
        if i < 20:
            y_list0.append(i)
    # if y_list[i] < 10:
    #     y_list[i] = 800
    # return y_list[i]  # TODO После цикла возвращаем index_list при помощи return


def move_snowflake(x_position=3, y_position=5):
    for i, y in enumerate(y_list):
        x_list[i] -= sd.random_number(-x_position, x_position)
        y_list[i] -= y_position
        point = sd.get_point(x_list[i], y_list[i])  # TODO Отлично, теперь только эту строку удалить
        # TODO И будет то, что нужно
