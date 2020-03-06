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
        x_list.append(sd.random_number(25, 1000))
        y_list.append(sd.random_number(100, 780))
        snowflake_size.append(sd.random_number(15, 35))


def snowflake_color(snowflake_count, color=sd.COLOR_WHITE):
    snowflake_creating(snowflake_count)
    for n in enumerate(y_list):
        move_snowflake(3, 5)


def snowflake_deleting(): # что то примерное, но создается всего одна
    if y_list[i] < 10:
        y_list[i] = 800
    return y_list[i]


def move_snowflake(x_position=3, y_position=5): # тут самому не нравится, что нагромоздил, но пока не вижу другого варианта
    for i, y in enumerate(y_list):              # и почему если запустить этот модуль, снединки начинают двигаться
        point = sd.get_point(x_list[i], y_list[i]) # но останавливаются внизу, хотя такого параметра тут нет нигде
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.background_color)
        x_list[i] -= sd.random_number(-x_position, x_position)
        y_list[i] -= y_position
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.COLOR_WHITE)
        snowflake_deleting()


snowflake_color(20) # опять вопросы, так получается вызвать функцию, а когда я так же хочу ее вызвать из 02_snowfall_module
# она не вызывается...

# TODO Тут нужны будут ещё две функции
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# TODO Первая с циклом по спискам, она должна вернуть список индексов
# TODO А вторая с циклом по этому списку индексов.


sd.pause()
