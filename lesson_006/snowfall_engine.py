# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 800)

x_list = []
y_list = []
snowflake_size = []
index_list = []


def snowflake_creating(snowflake_count):
    global x_list, y_list, snowflake_size
    x_list = []
    y_list = []
    snowflake_size = []
    for i in range(snowflake_count):
        x_list.append(sd.random_number(25, 1000))
        y_list.append(sd.random_number(100, 780))
        snowflake_size.append(sd.random_number(15, 35))


def snowflake_color(color=sd.COLOR_WHITE):
    global x_list, y_list
    for i, y in enumerate(y_list):
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=snowflake_size[i], color=color)


def snowflake_deleting():
    index_list = []
    for i, y in enumerate(y_list):
        if y < 20:
            index_list.append(i)
    return index_list


def move_snowflake(x_position=3, y_position=5):
    for i, y in enumerate(y_list):
        x_list[i] -= sd.random_number(-x_position, x_position)
        y_list[i] -= y_position


def remove_snowflake(index_list):
    for i in index_list:
        del index_list[-1]  # TODO Удалять надо из списков x_list, y_list, snowflake_size
        # TODO тут вместо -1 надо использовать индексы из index_list, т.е. подставлять вместо -1 - i
        # TODO В index_list записаны номера снежинок, которые надо удалить
        # TODO циклом мы проходим по списку, по-очереди номера передаются в i
        # Пример работы цикла изнутри:
        # index_list = [1, 2, 3]  -- создается список index_list, ему присваивается то, что передали параметром
        # i = 1  -- начинается первая итерация цикла
        # del x_list[i]
        # del y_list[i]
        # del snowflake_size[i]
        # i = 2
        # del x_list[i]
        # del y_list[i]
        # del snowflake_size[i]
        # i = 3
        # del x_list[i]
        # del y_list[i]
        # del snowflake_size[i]
        # TODO Перевернуть список можно при помощи среза список[::-1]
        # TODO И это желательно сделать до цикла
        # TODO index_list = index_list[::-1]
        # TODO и далее уже запускать цикл по индекс_лиск и удалять снежинки из 3 списков с координатами и размером


def new_snowflake_creating(snowflake_count):
    for i in range(snowflake_count):
        x_list.append(sd.random_number(25, 1000))
        y_list.append(sd.random_number(100, 780))
        snowflake_size.append(sd.random_number(15, 35))
