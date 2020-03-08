# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 800)

x_list = []
y_list = []
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
    for i in range(index_list):  # TODO тут просто используйте фор индекс ин индекс_лист
        # TODO Только сам index_list надо развернуть, чтобы удалялись снежинки с конца, а не с начала
        # TODO Тк удаление сдвигает все элементы после этой снежинки ([1, 2, 3] --> [1, 3])
        # TODO а если удаляем с конца, то сдвигаются те снежинки, которые мы уже не будет использовать
        if i in index_list:  # TODO Это условие будет не нужно тогда
            del index_list[i]

def new_snowflake_creating(snowflake_count):
    for i in range(snowflake_count):
        x_list.append(sd.random_number(25, 1000))
        y_list.append(sd.random_number(100, 780))
        snowflake_size.append(sd.random_number(15, 35))


# 1) Доделать функция snowflake_deleting вот тут не совсем понял, что надо доделать?
# TODO Теперь всё ок, я имел ввиду доделать то, что я в тудушке написал