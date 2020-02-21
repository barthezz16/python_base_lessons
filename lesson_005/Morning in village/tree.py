# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
sd.background_color = (255, 255, 255)


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


def branch(point, angle, length):
    if length < 1:
        return
    if 1 < length < 10:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v1.draw(color=sd.COLOR_DARK_GREEN)
    else:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v1.draw(color=sd.COLOR_DARK_ORANGE)
        next_length = length * .75
        angle_1 = angle + 30
        angle_2 = angle - 30
        branch(point=v1.end_point, angle=angle_1, length=next_length)
        branch(point=v1.end_point, angle=angle_2, length=next_length)


point_0 = sd.get_point(800, 0)
angle_0 = 90
length = 100

branch(point=point_0, angle=angle_0, length=length)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


# зачет!
