# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

import simple_draw as sd

sd.set_screen_size(900, 900)

# def triangle(triangle_point, angle=0, ):
#     first_line = sd.get_vector(start_point=triangle_point, angle=angle, length=200, width=3)
#     first_line.draw()
#
#     second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 120, length=200, width=3)
#     second_line.draw()
#
#     sd.line(start_point=second_line.end_point, end_point=triangle_point, width=3)
#
#
# def square(square_point, angle=0):
#     first_line = sd.get_vector(start_point=square_point, angle=0, length=200, width=3)
#     first_line.draw()
#
#     second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 90, length=200, width=3)
#     second_line.draw()
#
#     third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 180, length=200, width=3)
#     third_line.draw()
#
#     sd.line(start_point=third_line.end_point, end_point=square_point, width=3)
#
#
# def pentagon(pentagon_point, angle=0):
#     first_line = sd.get_vector(start_point=pentagon_point, angle=0, length=150, width=3)
#     first_line.draw()
#
#     second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 72, length=150, width=3)
#     second_line.draw()
#
#     third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 144, length=150, width=3)
#     third_line.draw()
#
#     fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 216, length=150, width=3)
#     fourth_line.draw()
#
#     sd.line(start_point=fourth_line.end_point, end_point=pentagon_point, width=3)
#
#
# def hexagon(hexagon_point, angle=0):
#     first_line = sd.get_vector(start_point=hexagon_point, angle=0, length=125, width=3)
#     first_line.draw()
#
#     second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 60, length=125, width=3)
#     second_line.draw()
#
#     third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 120, length=125, width=3)
#     third_line.draw()
#
#     fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 180, length=125, width=3)
#     fourth_line.draw()
#
#     fifth_line = sd.get_vector(start_point=fourth_line.end_point, angle=angle + 240, length=125, width=3)
#     fifth_line.draw()
#
#     sd.line(start_point=fifth_line.end_point, end_point=hexagon_point, width=3)
#
#
# def triangle(triangle_point, angle=0, ):
#     first_line = sd.get_vector(start_point=triangle_point, angle=angle, length=200, width=3)
#     first_line.draw()
#
#     second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 120, length=200, width=3)
#     second_line.draw()
#
#     sd.line(start_point=second_line.end_point, end_point=triangle_point, width=3)
point = sd.get_point(400, 400)


#
def figures(start_point=point, angle=0, length=200, width=3):
    line = sd.get_vector(start_point, angle, length, width)
    line.draw()
    return line.end_point


def shapes_draw(start_point, end_point, next_angle=0, length=200, width=3, angle_step=0):
    for angle in range(0, 360 - angle_step, angle_step):
        start_point = figures(start_point, angle, length, width)
    else:
        sd.line(start_point=start_point, end_point=end_point, width=3)


length = 200

start_point_hexagon_x = point.x + 150
start_point_hexagon_y = point.y - 150
start_point_pentagon_x = point.x - 150
start_point_pentagon_y = point.y - 150
start_point_square_x = point.x - 150
start_point_square_y = point.y + 150
start_point_triangle_x = point.x + 150
start_point_triangle_y = point.y + 150

triangle_point = sd.get_point(start_point_triangle_x, start_point_triangle_y)
hexagon_point = sd.get_point(start_point_hexagon_x, start_point_hexagon_y)
pentagon_point = sd.get_point(start_point_pentagon_x, start_point_pentagon_y)
square_point = sd.get_point(start_point_square_x, start_point_square_y)
triangle_angle = 120
square_angle = 90
pentagon_angle = 72
hexagon_angle = 60

shapes_draw(start_point=triangle_point, end_point=triangle_point, next_angle=triangle_angle, length=length, width=3,
            angle_step=triangle_angle)
shapes_draw(start_point=square_point, end_point=square_point, next_angle=square_angle, length=length, width=3,
            angle_step=square_angle)
shapes_draw(start_point=pentagon_point, end_point=pentagon_point, next_angle=pentagon_angle, length=150, width=3,
            angle_step=pentagon_angle)
shapes_draw(start_point=hexagon_point, end_point=hexagon_point, next_angle=hexagon_angle, length=125, width=3,
            angle_step=hexagon_angle)

# for angle in range(0, 360 - triangle_angle, triangle_angle):
#     print(angle, 'треугольник')
#     next_point = figures(start_point=next_point, angle=angle, length=200, width=3)
# else:
#     sd.line(start_point=next_point, end_point=triangle_point, width=3)
# next_point = square_point
# for angle in range(0, 360 - square_angle, square_angle):
#     print(angle, 'квадрат')
#     next_point = figures(start_point=next_point, angle=angle, length=200, width=3)
# else:
#     sd.line(start_point=next_point, end_point=square_point, width=3)
#     next_point = pentagon_point
# for angle in range(0, 360 - pentagon_angle, pentagon_angle):
#     print(angle, 'пятиугольник')
#     next_point = figures(start_point=next_point, angle=angle, length=150, width=3)
# else:
#     sd.line(start_point=next_point, end_point=pentagon_point, width=3)
# next_point = hexagon_point
# for angle in range(0, 360 - hexagon_angle, hexagon_angle):
#     print(angle, 'шестиугольник')
#     next_point = figures(start_point=next_point, angle=angle, length=125, width=3)
# else:
#     sd.line(start_point=next_point, end_point=hexagon_point, width=3)


# сделал так, потому что не совсем понял что именно надо, если сделать один цикл для всех фигур, то надо же еще
# менять стартовую точку для фигуры и последнюю точку для последней линии, чтобы не было разрыва.
# TODO нужен не цикл, нужна ФУНКЦИЯ
# TODO деф общая_функция(start_point, angle, length, width, шаг_угла)
# TODO     а тут уже цикл и прочее
# triangle(triangle_point)
# square(square_point)
# pentagon(pentagon_point)
# hexagon(hexagon_point)

sd.pause()
# определить функци
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
