# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 800)


# x_list = []
# y_list = []
# snowflake_size = []
# for i in range(20):
#     x_list.append(sd.random_number(25, 350))
#     y_list.append(sd.random_number(800, 880))
#     snowflake_size.append(sd.random_number(15, 36))
#
#
# def snowfall_draw():
#     while True:
#         sd.start_drawing()
#         for i, y in enumerate(y_list):
#             point = sd.get_point(x_list[i], y_list[i])
#             sd.snowflake(center=point, length=snowflake_size[i], color=sd.background_color)
#             x_list[i] -= sd.random_number(-3, 3)
#             y_list[i] -= 5
#             point = sd.get_point(x_list[i], y_list[i])
#             sd.snowflake(center=point, length=snowflake_size[i], color=sd.COLOR_WHITE)
#         sd.finish_drawing()
#         sd.sleep(.05)
#         if sd.user_want_exit() or y_list[i] <= 25:
#             break


def snowflake_creating(snowflake_count):
    global x_list, y_list, snowflake_size, i, point
    x_list = []
    y_list = []
    snowflake_size = []
    for i in range(snowflake_count):
        x_list.append(sd.random_number(25, 600))
        y_list.append(sd.random_number(700, 780))
        snowflake_size.append(sd.random_number(15, 36))


def snowflake_color(snowflake_count, color):
    snowflake_creating(snowflake_count=snowflake_count)  # TODO Тут эту функцию вызывать не нужно
    # TODO Она будет вызвана отдельно, в главном модуле
    # TODO Иначе каждый раз при рисовании списки будут обновляться и снежинки не будут падать
    for i, y in enumerate(y_list):
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point)  # TODO кстати сюда ещё стоит передавать параметр color


def move_snowflake(x=3, y=5):  # TODO тк у параметра имя 'y'
    for i, y in enumerate(y_list):  # TODO и у переменной цикла такое же имя, то используется переменная, а не параметр
        # TODO используйте разные имена
        x_list[i] -= sd.random_number(-x, x)
        y_list[i] -= y


# TODO Тут нужны будут ещё две функции
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# TODO Первая с циклом по спискам, она должна вернуть список индексов
# TODO А вторая с циклом по этому списку индексов.
def snowflake_deleting():
    pass


# snowflake_color(snowflake_count, color=sd.COLOR_WHITE)

sd.pause()
