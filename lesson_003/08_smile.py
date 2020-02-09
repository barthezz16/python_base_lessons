# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
# TODO Рисование смайлика надо вынести в отдельную функцию
# TODO И точки для каждого элемента связать между собой через x и y
# TODO Например если центр x, y, то глаз x + 10, y + 10 или что-то вроде этого
# TODO Тогда можно будет передавать функции случайную точку, а вокруг неё отрисуются все элементы смайлика
def smile(point):
    point = sd.get_point(100, 100)
    smile_start_x = 152
    smile1_y = 270
    smile_end_x = smile_start_x + 45
    start_position = sd.get_point(smile_start_x, smile1_y)
    end_position = sd.get_point(smile_end_x, smile1_y)
    sd.line(start_point=start_position, end_point=end_position)
    radius = 10
    for x in range(150, 201, 50):
        point = sd.get_point(x, 300)
        sd.circle(center_position=point, radius=radius, width=2)
        point = sd.get_point(175, 290)
        radius = 10
        sd.circle(center_position=point, radius=50, width=2)
    smile(sd.random_point())


for _ in range(10):
    smile(point=sd.random_point())

sd.pause()

sd.pause()
