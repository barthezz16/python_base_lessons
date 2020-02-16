# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

root_point = sd.get_point(600, 0)


def draw_branches(point, angle, length):
    # TODO Примерный код, с объяснениями показан в лекции
    # https://go.skillbox.ru/course/python-razrabotchik-s-nulya/5e939d5a-3ae1-4548-9a61-a6aae4d6c644
    # TODO Начиная с 14-ой минуты идёт подробное объяснение этого алгоритма
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    return v1.end_point
# TODO Только там пример ограничивается одним вызовом функцией самой себя, а нам нужно будет 2 вызова
# TODO Чтобы мы передавали одну точку в два вызова функции с разными углами,
# TODO тогда из этой точки будет нарисовано 2 ветви


# TODO тут тоже вроде все на теории понятно, но как застваить функцию принимать последнии координаты линии не пойму,
# TODO особенно потом, когда линий будет все больше...


angle_0 = 90
length_0 = 200
next_point = draw_branches(point=root_point, angle=angle_0, length=length_0)
first_angle = angle_0 - 30
next_length = length_0 * .75
first_point = draw_branches(point=next_point, angle=first_angle, length=next_length)
second_angle = angle_0 + 30
second_point = draw_branches(point=next_point, angle=second_angle, length=next_length)

point_0 = sd.get_point(600, 0)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()