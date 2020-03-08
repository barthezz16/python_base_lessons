# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 800)

x_list = []
y_list = []
index_list = []
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
    # TODO Если используется index_list снаружи - то надо указать на это при помощи global
    # TODO + тут надо его будет обновлять, иначе при повторном вызове в список попадут дубли
    # TODO а если прописать здесь index_list = [] -- то каждый раз список будет с 0 формироваться, без копий
    for i, y in enumerate(y_list):
        if y < 20:
            index_list.append(i)
    return index_list


def move_snowflake(x_position=3, y_position=5):
    for i, y in enumerate(y_list):
        x_list[i] -= sd.random_number(-x_position, x_position)
        y_list[i] -= y_position


# TODO Сейчас снегопад уже работает но надо наладить удаление/добавление новых снежинок
# TODO Для этого надо:
# TODO 1) Доделать функция snowflake_deleting
# TODO 2) Сделать функцию, которая будет проходить по глобальному index_list и удалять снежинки, которые там записаны
# TODO 3) Сделать функцию, которая будет добавлять снежинки. Это будет копия snowflake_creating, только без
# TODO обнуления списков. просто убрать эти строки из копии
# x_list = []
#     y_list = []
#     snowflake_size = []
