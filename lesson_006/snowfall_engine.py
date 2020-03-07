# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 800)

def snowflake_creating(snowflake_count):
    global x_list, y_list, snowflake_size, i, point  # TODO тут 'point' и 'i' не нужны
    # TODO а списки x_list, y_list, snowflake_size надо будет ещё вне функций создать
    # TODO global говорит о том, что искать эти названия надо вне функции
    # TODO сейчас вне функции их нет, просто продублируйте снаружи:
    # x_list = []
    # y_list = []
    # snowflake_size = []

    # TODO Эти же строки пусть остаются и здесь. Логика следующая:
    # TODO Пайтону указываем, что искать списки надо снаружи в "глобальном" пространстве
    # TODO Дальше эти списки обновляются здесь на всякий случай, а потом заполняются.
    x_list = []
    y_list = []
    snowflake_size = []
    for i in range(snowflake_count):
        x_list.append(sd.random_number(25, 1000))
        y_list.append(sd.random_number(100, 780))
        snowflake_size.append(sd.random_number(15, 35))


def snowflake_color(snowflake_count, color=sd.COLOR_WHITE):
    snowflake_creating()  # TODO Это тоже удаляем
    global point  # TODO И это.
    # TODO Глобальными вместо point надо объявить списки y_list, x_list
    for i, y in enumerate(y_list):
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.background_color)



def snowflake_deleting():
    # TODO Здесь цикл по снежинкам, проверка 'y' координаты, добавление этой координаты в новый список
    # TODO Обновлять координату не нужно
    if y_list[i] < 10:
        y_list[i] = 800
    return y_list[i]


def move_snowflake(x_position=3, y_position=5):
    # TODO Здесь цикл по снежинкам, с изменением координат (42, 43 строка)
    # TODO создание точек, snowflake_deleting и sd.snowflake - удалить
    x_list[i] -= sd.random_number(-x_position, x_position)
    y_list[i] -= y_position
    point = sd.get_point(x_list[i], y_list[i])


# опять вопросы, так получается вызвать функцию, а когда я так же хочу ее вызвать из 02_snowfall_module
# она не вызывается...

# TODO Тут нужны будут ещё две функции
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# TODO Первая с циклом по спискам, она должна вернуть список индексов
# TODO А вторая с циклом по этому списку индексов.


sd.pause()
