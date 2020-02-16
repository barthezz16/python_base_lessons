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


def triangle(triangle_point, angle=0, ):
    first_line = sd.get_vector(start_point=triangle_point, angle=angle, length=200, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 120, length=200, width=3)
    second_line.draw()

    sd.line(start_point=second_line.end_point, end_point=triangle_point, width=3)


def square(square_point, angle=0):
    first_line = sd.get_vector(start_point=square_point, angle=0, length=200, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 90, length=200, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 180, length=200, width=3)
    third_line.draw()

    sd.line(start_point=third_line.end_point, end_point=square_point, width=3)


def pentagon(pentagon_point, angle=0):
    first_line = sd.get_vector(start_point=pentagon_point, angle=0, length=150, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 72, length=150, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 144, length=150, width=3)
    third_line.draw()

    fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 216, length=150, width=3)
    fourth_line.draw()

    sd.line(start_point=fourth_line.end_point, end_point=pentagon_point, width=3)


def hexagon(hexagon_point, angle=0):
    first_line = sd.get_vector(start_point=hexagon_point, angle=0, length=125, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 60, length=125, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 120, length=125, width=3)
    third_line.draw()

    fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 180, length=125, width=3)
    fourth_line.draw()

    fifth_line = sd.get_vector(start_point=fourth_line.end_point, angle=angle + 240, length=125, width=3)
    fifth_line.draw()

    sd.line(start_point=fifth_line.end_point, end_point=hexagon_point, width=3)

# TODO Обратите внимание как я перенес ваш код. Структура программы сейчас такая Импорты >> Определение функций >> код
# TODO Таким же образом надо будет отформатировать 2 и 3 модули
length = 200
point = sd.get_point(400, 400)

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

triangle(triangle_point)
square(square_point)
pentagon(pentagon_point)
hexagon(hexagon_point)

sd.pause()
# определить функци
# TODO Можете приступать ко второй части!
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
