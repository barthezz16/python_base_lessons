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


def get_polygon(n):
    def figures(start_point=point, angle=0, length=200, width=3):
        line = sd.get_vector(start_point, angle, length, width)
        line.draw()
        return get_polygon(n)
    return figures(figures())


def shapes_draw(start_point, end_point, next_angle=0, length=200, width=3, angle_step=0):
    for angle in range(0, 360 - angle_step, angle_step):
        start_point = figures(start_point, angle + next_angle, length, width)  # Чтобы можно было "крутить" фигуры
    else:
        sd.line(start_point=start_point, end_point=end_point, width=3)
    #  здесь ваш код
    # Максим, тут ппосто темный лес, я просто не понимаю что тут надо сделать, и с чего начать...
    # TODO Здесь вам нужно внутри этой функции инициализировать общую функцию из 04.01
    # TODO И возвращать после инициализации функцию для конкретной фигуры
    # TODO Чтобы из общей сделать конкретную функцию - нужно завязать функцию на использовании параметра "n"
    # TODO У вас там общая функция рисует нужную в зависимости от angle_step
    # TODO Значит здесь вам нужно создать переменную angle_step, которая будет изменяться от n
    # TODO что-то вроде angle_step = 360//n
    # TODO После этого используйте этот angle_step в общей функции и верните получившуюся функцию:
    # 1) angle_step = 360//n
    # 2) деф общая функция с использованием конкретного угла, заданного выше
    # 3) return общая_функция

draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()

point = sd.get_point(400, 400)
# def figures(start_point=point, angle=0, length=200, width=3):
#     line = sd.get_vector(start_point, angle, length, width)
#     line.draw()
#     return line.end_point
#
#
# def shapes_draw(start_point, end_point, next_angle=0, length=200, width=3, angle_step=0):
#     for angle in range(0, 360 - angle_step, angle_step):
#         start_point = figures(start_point, angle + next_angle, length, width)  # Чтобы можно было "крутить" фигуры
#     else:
#         sd.line(start_point=start_point, end_point=end_point, width=3)
#
#
# length = 200
#
# start_point_hexagon_x = point.x + 150
# start_point_hexagon_y = point.y - 150
# start_point_pentagon_x = point.x - 150
# start_point_pentagon_y = point.y - 150
# start_point_square_x = point.x - 150
# start_point_square_y = point.y + 150
# start_point_triangle_x = point.x + 150
# start_point_triangle_y = point.y + 150
#
# triangle_point = sd.get_point(start_point_triangle_x, start_point_triangle_y)
# hexagon_point = sd.get_point(start_point_hexagon_x, start_point_hexagon_y)
# pentagon_point = sd.get_point(start_point_pentagon_x, start_point_pentagon_y)
# square_point = sd.get_point(start_point_square_x, start_point_square_y)
# triangle_angle = 120
# square_angle = 90
# pentagon_angle = 72
# hexagon_angle = 60
#
# shapes_draw(start_point=triangle_point, end_point=triangle_point, next_angle=triangle_angle, length=length, width=3,
#             angle_step=triangle_angle)
# shapes_draw(start_point=square_point, end_point=square_point, next_angle=square_angle, length=length, width=3,
#             angle_step=square_angle)
# shapes_draw(start_point=pentagon_point, end_point=pentagon_point, next_angle=pentagon_angle, length=150, width=3,
#             angle_step=pentagon_angle)
# shapes_draw(start_point=hexagon_point, end_point=hexagon_point, next_angle=hexagon_angle, length=125, width=3,
#             angle_step=hexagon_angle)
#
# sd.pause()
