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

length = 200
point = sd.get_point(400, 400)
start_point_triangle_x = point.x + 150
start_point_triangle_y = point.y + 150
triangle_point = sd.get_point(start_point_triangle_x, start_point_triangle_y)

# TODO Подобный тип кода(создание функций - def), который создает какой-то инструмент для дальнейшего использования
# TODO Но сам по себе ничего не делает - надо располагать в начале, а "исполняемый" код
# TODO В частности вызов функций - после этого "подготовительного" кода)
def triangle(triangle_point, angle=0):
    first_line = sd.get_vector(start_point=triangle_point, angle=0, length=200, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 120, length=200, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 240, length=200, width=3)
    third_line.draw()
# TODO Если приблизить итоговую фигуру, нарисованную векторами, будет заметен разрыв между последней стороной
# TODO и начальной точкой.
# TODO Этот разрыв надо убрать.
# TODO Происходит это потому, что вектор рисуется из одной точки, а координаты второй рассчитываются
# TODO Расчёты округляются до целых чисел (тк нельзя нарисовать пол пикселя)
# TODO Из-за этого появляются неточности, которые копятся с каждой стороной и в итоге происходит разрыв.
# TODO В нашем случае решить это можно с помощью sd.line() вместо последнего вектора.

triangle(triangle_point)

start_point_square_x = point.x - 150
start_point_square_y = point.y + 150
square_point = sd.get_point(start_point_square_x, start_point_square_y)


def square(square_point, angle=0):
    # TODO Помимо прочего можно заменить дублирование векторов вручную циклом
    # TODO Цикл можно использовать не только для нужного количества итераций
    # TODO Но так же и для расчёта нужных значений переменных.
    # TODO Так мы можем задать цикл по значениям угла с нужным нам шагом и не считать угол отдельной операцией
    # TODO Например для треугольнкиа это будет: for angle in range(0, 360 - 120, 120)
    # TODO angle будет на первой итерации равен 0, на второй 120 (от третьей мы избавились отняв от 360 120)

    first_line = sd.get_vector(start_point=square_point, angle=0, length=200, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 90, length=200, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 180, length=200, width=3)
    third_line.draw()

    fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 270, length=200, width=3)
    fourth_line.draw()


square(square_point)

start_point_pentagon_x = point.x - 150
start_point_pentagon_y = point.y - 150
pentagon_point = sd.get_point(start_point_pentagon_x, start_point_pentagon_y)


def pentagon(pentagon_point, angle=0):
    first_line = sd.get_vector(start_point=pentagon_point, angle=0, length=150, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 72, length=150, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 144, length=150, width=3)
    third_line.draw()

    fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 216, length=150, width=3)
    fourth_line.draw()

    fifth_line = sd.get_vector(start_point=fourth_line.end_point, angle=angle + 288, length=150, width=3)
    fifth_line.draw()


pentagon(pentagon_point)

start_point_hexagon_x = point.x + 150
start_point_hexagon_y = point.y - 150
hexagon_point = sd.get_point(start_point_hexagon_x, start_point_hexagon_y)


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

    sixth_line = sd.get_vector(start_point=fifth_line.end_point, angle=angle + 300, length=125, width=3)
    sixth_line.draw()


hexagon(hexagon_point)

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
