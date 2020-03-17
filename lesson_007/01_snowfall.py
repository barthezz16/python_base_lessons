# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        # TODO Списки тут не нужны
        # TODO у одной снежинки - пара координат (x, y)
        self.x_list = []
        self.y_list = []
        self.snowflake_size = []
        self.index_list = []
        self.x_list.append(sd.random_number(25, 1170))
        self.y_list.append(sd.random_number(0, 800))
        self.snowflake_size.append(sd.random_number(15, 35))

    def draw(self, color=sd.COLOR_WHITE):
        for i, y in enumerate(self.y_list):  # TODO Здесь и дальше все циклы убираем
            point = sd.get_point(self.x_list[i], self.y_list[i])
            sd.snowflake(center=point, length=self.snowflake_size[i], color=color)

    def move(self, x_position=3, y_position=5):
        for i, y in enumerate(self.y_list):
            self.x_list[i] -= sd.random_number(-x_position, x_position)
            self.y_list[i] -= y_position

    def can_fall(self):
        for i, y in enumerate(self.y_list):
            if y < 20:  # TODO В этом методе нужно будет возвращать True/False в зависимости от того может ли
                # TODO эта снежинка упасть. Можно в одну строчку это реализовать, возвращая это условие
                self.index_list.append(i)
        return self.index_list

    def clear_previous_picture(self):
        sd.clear_screen()  # TODO Тут очистку лучше производить рисованием снежинки в текущей точке цветом фона


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

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
