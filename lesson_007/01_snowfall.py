# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = (sd.random_number(25, 1170))
        self.y = sd.random_number(700, 1000)
        self.snowflake_size = sd.random_number(15, 35)
        self.index_list = []

    def draw(self, color=sd.COLOR_WHITE):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.snowflake_size, color=color)

    def move(self, x_position=2, y_position=4):
        self.x -= sd.random_number(-x_position, x_position)
        self.y -= y_position

    def can_fall(self):
        return self.y > 20

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.snowflake_size, color=sd.background_color)


def get_flakes(count):
    for i in range(count):
        flake_list.append(Snowflake())
    return flake_list


def get_fallen_flakes():
    fallen_flakes = []
    for i, y in enumerate(flake_list):
        if not flake.can_fall():
            fallen_flakes.append(i)
    fallen_flakes = fallen_flakes[::-1]
    for count_1 in fallen_flakes:
        del fallen_flakes[count_1]
    return fallen_flakes


def append_flakes(count):
    for i in range(count):
        flake_list.append(Snowflake()) # TODO а тут согласен... мы же просто создаем новые объекты,
        # TODO ничего не надо возвращать


flake_list = []
flake = Snowflake()
flakes = get_flakes(count=50)
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()
    if fallen_flakes:
        append_flakes(count=len(fallen_flakes))  # TODO вот тут как раз я и не могу понять,
        # TODO просто тут так было изначально написано что принимает список,
        # TODO вот я и думал что надо под этот код подстроить и не понял как...
    sd.sleep(0.05)
    if sd.user_want_exit():
        break

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#  Можете приступать к шагу №2
#  Тут нужно будет реализовать несколько отдельных функций
#  Которые будут запускать множество таких снежинок
# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
