# -*- coding: utf-8 -*-

import simple_draw as sd

sd.set_screen_size(900, 900)


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
def figures(start_point, angle=0, length=200, width=3):
    line = sd.get_vector(start_point, angle, length, width)
    line.draw()
    return line.end_point


def get_polygon(n):
    angle_step = 360 // n

    def shapes_draw(start_point, end_point, next_angle=0, length=200, width=3):
        for angle in range(0, 360 - angle_step, angle_step):
            start_point = figures(start_point, angle + next_angle, length, width)
        else:
            sd.line(start_point=start_point, end_point=end_point, width=3)

    return shapes_draw


draw_triangle = get_polygon(n=3)
triangle_point = sd.get_point(600, 600)
draw_triangle(start_point=triangle_point, end_point=triangle_point, next_angle=0, length=200, width=3)


draw_square = get_polygon(n=4)
square_point = sd.get_point(200, 600)
draw_square(start_point=square_point, end_point=square_point, next_angle=0, length=200, width=3)


draw_pentagon = get_polygon(n=5)
pentagon_point = sd.get_point(200, 200)
draw_pentagon(start_point=pentagon_point, end_point=pentagon_point, next_angle=0, length=200, width=3)


draw_hexagon = get_polygon(n=6)
hexagon_point = sd.get_point(600, 200)
draw_hexagon(start_point=hexagon_point, end_point=hexagon_point, next_angle=0, length=150, width=3)
sd.pause()
#зачет!