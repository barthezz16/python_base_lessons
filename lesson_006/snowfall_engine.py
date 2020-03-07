# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 800)

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
    # TODO В этой функции должен быть только цикл по снежинкам и функция рисования snowflake
    # TODO move_snowflake - удалить
    move_snowflake(3, 5)
    sd.snowflake(center=point, length=snowflake_size[i], color=sd.COLOR_WHITE)
    for n in enumerate(y_list):
        move_snowflake(3, 5)


def snowflake_deleting():
    # TODO Здесь цикл по снежинкам, проверка 'y' координаты, добавление этой координаты в новый список
    # TODO Обновлять координату не нужно
    if y_list[i] < 10:
        y_list[i] = 800
    return y_list[i]


def move_snowflake(x_position=3, y_position=5):
    # TODO Здесь цикл по снежинкам, с изменением координат (42, 43 строка)
    # TODO создание точек, snowflake_deleting и sd.snowflake - удалить
    global point
    for i, y in enumerate(y_list):
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.background_color)
        x_list[i] -= sd.random_number(-x_position, x_position)
        y_list[i] -= y_position
        point = sd.get_point(x_list[i], y_list[i])

        snowflake_deleting()


snowflake_color(20)
# опять вопросы, так получается вызвать функцию, а когда я так же хочу ее вызвать из 02_snowfall_module
# она не вызывается...

# TODO Тут нужны будут ещё две функции
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# TODO Первая с циклом по спискам, она должна вернуть список индексов
# TODO А вторая с циклом по этому списку индексов.


sd.pause()
