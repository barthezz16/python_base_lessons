# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 800)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

x_list = []
y_list = []
snowflake_size = []
for i in range(20):
    x_list.append(sd.random_number(25, 350))
    y_list.append(sd.random_number(800, 880))
    snowflake_size.append(sd.random_number(15, 36))


def snowfall_draw():
    while True:
        sd.start_drawing()
        for i, y in enumerate(y_list):
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=snowflake_size[i], color=sd.background_color)
            x_list[i] -= sd.random_number(-5, 5)
            y_list[i] -= 5
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=snowflake_size[i], color=sd.COLOR_WHITE)
        sd.finish_drawing()
        sd.sleep(.01)
        if sd.user_want_exit() or y_list[i] <= 25:
            break


if __name__ == '__main__':
    snowfall_draw()



# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
# зачет!
