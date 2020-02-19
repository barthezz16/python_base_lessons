# -*- coding: utf-8 -*-
import simple_draw as sd

sd.set_screen_size(900, 900)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
def figures(start_point=sd.get_point(400, 400), angle=0, length=200, width=3):
    line = sd.get_vector(start_point, angle, length, width)
    line.draw(color=colors[color_number])
    return line.end_point


def shapes_draw(start_point, end_point, next_angle=0, length=200, width=3, angle_step=0):
    for angle in range(0, 360 - angle_step, angle_step):
        start_point = figures(start_point, angle + next_angle, length, width)
    else:
        sd.line(start_point=start_point, end_point=end_point, color=colors[color_number], width=3)


sd.set_screen_size(900, 900)

point = sd.get_point(400, 400)

colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN,
          sd.COLOR_BLUE, sd.COLOR_PURPLE)

print('Возможные цвета', '\n', '0 : red', '\n', '1 : orange', '\n', '2 : yellow', '\n', '3 : green', '\n',
      '4 : cyan', '\n', '5 : blue', '\n', '6 : purple')

while True:
    user_input = input("Введите желаемый цвет ")
    color_number = int(user_input)
    if color_number <= len(colors) - 1:
        break
    else:
        print('Введен некорректный номер')

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

sd.pause()

sd.pause()
#зачет!