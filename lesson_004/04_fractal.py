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
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    return v1.end_point


# def draw_branches(point, angle, length):
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     angle_1 = angle + 30
#     angle_2 = angle - 30
#     v2 = sd.get_vector(start_point=point, angle=angle_1, length=length, width=3)
#     v3 = sd.get_vector(start_point=point, angle=angle_2, length=length, width=3)
#


# Только там пример ограничивается одним вызовом функцией самой себя, а нам нужно будет 2 вызова
# Чтобы мы передавали одну точку в два вызова функции с разными углами,
# тогда из этой точки будет нарисовано 2 ветви
# тут тоже вроде все на теории понятно, но как застваить функцию принимать последнии координаты линии не пойму,
# особенно потом, когда линий будет все больше...
# деф бранч(точка, угол, длина)
#     условие остановки рекурсии (в лекции есть)
#     рисование_вектора(точка, угол, длина)
#     расчёт_новых_углов
#     бранч(новая_точка, угол1, длина)
#     бранч(новая_точка, угол2, длина)

def branch(point, angle, length):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    angle_1 = angle + 30
    angle_2 = angle - 30
    # TODO Вместо векторов тут нужны вызовы функции branch (самой себя)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle_1, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v1.end_point, angle=angle_2, length=length, width=3)
    v3.draw()
    return v1.end_point  # TODO И ретурн не нужен будет


angle_0 = 90
length_0 = 200
next_point = branch(point=root_point, angle=angle_0, length=length_0)
first_angle = angle_0 - 30
next_length = length_0 * .75
first_point = branch(point=next_point, angle=first_angle, length=next_length)
second_angle = angle_0 + 30
second_point = branch(point=next_point, angle=second_angle, length=next_length)

point_0 = sd.get_point(600, 0)

# TODO тут уперся в это

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
