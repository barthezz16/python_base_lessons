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
        self.y = sd.random_number(500, 800)
        self.snowflake_size = sd.random_number(15, 35)
        self.index_list = []

    def draw(self, color=sd.COLOR_WHITE):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.snowflake_size, color=color)

    def move(self, x_position=2, y_position=7):
        self.x -= sd.random_number(-x_position, x_position)
        self.y -= y_position

    def can_fall(self):
        return self.y > 20

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.snowflake_size, color=sd.background_color)


def get_flakes(count):
    flake = Snowflake()
    for i in range(count):
        flake_list.append(flake)  # TODO вместо flake нужно сюда поместить Snowflake()
        # TODO Snowflake() - срабатывает и создает объект класса
        # TODO Если его вызвать до цикла, то вы добавите в список много одинаковых объектов
        # TODO А если внутри цикла вызывать Snowflake() то каждый раз будет создаваться новый объект-снежинка
        return flake_list  # не пойму, почему не добавляются снижинки в список...
        # TODO Обратите внимание на отступ, return срабатывает сразу же на первой итерации цикла
    # TODO Обрывает его выполнение и завершает функцию, добавив всего одну снежинку

def get_fallen_flakes():
    fallen_flakes = []
    # TODO Тут нужно пройти по списку снежинок и записывать их индексы в списке, а не сами снежинки
    if flake.y < -36:  # TODO Используйте тут метод снежинок can_fall, только с приставкой not
        fallen_flakes.append(flake)
    return fallen_flakes


def append_flakes(count):
    # TODO И тут нужен цикл. И вообще функция должна принимать список параметром - изменять его - возвращать ретурном
    flake.x = (sd.random_number(25, 1170))
    flake.y = sd.random_number(500, 800)
    flake.snowflake_size = sd.random_number(15, 35)


flake_list = []
flake = Snowflake()
N = 30
flakes = get_flakes(count=N)
print(len(flakes))
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()
    if fallen_flakes:
        append_flakes(count=fallen_flakes)
    sd.sleep(0.1)
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
