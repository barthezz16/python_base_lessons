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
        point = sd.get_point(x_list[i], y_list[i])  # TODO Эта строка тут кажется лишней
        # TODO В список она не попадает (да вроде и не должна попадать), просто создается
        # TODO И пересоздается на каждой итерации, переписывая себя



def snowflake_color(snowflake_count, color):
    snowflake_creating(snowflake_count=snowflake_count)
    # TODO А вот здесь уже стоит циклом пройти по спискам и создавать для каждой пары координат точку
    # TODO И эту точку использовать в функции рисования.
    # TODO Сейчас при вызове функции сперва отработает цикл, и только потом, один раз вызовется функция
    # TODO рисования снежинки.
    sd.snowflake(center=point, length=snowflake_size[i], color=color)


def move_snowflake(x, y):
    # TODO И тут надо цикл сделать.
    # TODO Сейчас эта функция будет использовать одно значение i, скорее всего последнее, которое было в цикле
    # TODO И сдвинется только одна снежинка
    x_list[i] -= sd.random_number(-x, x)
    y_list[i] -= y
    point = sd.get_point(x_list[i], y_list[i])  # TODO А этот point опять уйдет в никуда, его можно удалить
    # TODO Точки создавать лучше в функции рисования


# TODO Тут нужны будут ещё две функции
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# TODO Первая с циклом по спискам, она должна вернуть список индексов
# TODO А вторая с циклом по этому списку индексов.
def snowflake_deleting():
    pass

# snowflake_color(snowflake_count, color=sd.COLOR_WHITE)

sd.pause()