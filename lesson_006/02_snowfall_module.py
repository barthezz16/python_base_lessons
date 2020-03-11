# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall_engine import snowflake_creating, snowflake_color, move_snowflake, snowflake_deleting, \
    new_snowflake_creating, remove_snowflake

sd.resolution = (1200, 800)

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)

snowflake_numbers = 100
snowflake_creating(snowflake_numbers)
while True:
    sd.start_drawing()
    snowflake_color(color=sd.background_color)
    move_snowflake(3, 6)
    snowflake_color(color=sd.COLOR_WHITE)
    index_list = snowflake_deleting()
    if index_list:
        remove_snowflake(index_list)
        new_snowflake_creating(len(index_list))
    sd.finish_drawing()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break

sd.pause()
#зачет!