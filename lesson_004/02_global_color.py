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
point = sd.get_point(400, 400)
start_point_triangle_x = point.x + 150
start_point_triangle_y = point.y + 150
triangle_point = sd.get_point(start_point_triangle_x, start_point_triangle_y)


def triangle(triangle_point, angle=0):
    first_line = sd.get_vector(start_point=triangle_point, angle=angle, length=200, width=3)
    first_line.draw(color=colors[color_number])

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 120, length=200, width=3)
    second_line.draw(color=colors[color_number])

    sd.line(start_point=second_line.end_point, end_point=triangle_point, width=3, color=colors[color_number])


start_point_square_x = point.x - 150
start_point_square_y = point.y + 150
square_point = sd.get_point(start_point_square_x, start_point_square_y)


def square(square_point, angle=0):
    first_line = sd.get_vector(start_point=square_point, angle=0, length=200, width=3)
    first_line.draw(color=colors[color_number])

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 90, length=200, width=3)
    second_line.draw(color=colors[color_number])

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 180, length=200, width=3)
    third_line.draw(color=colors[color_number])

    sd.line(start_point=third_line.end_point, end_point=square_point, width=3, color=colors[color_number])


start_point_pentagon_x = point.x - 150
start_point_pentagon_y = point.y - 150
pentagon_point = sd.get_point(start_point_pentagon_x, start_point_pentagon_y)


def pentagon(pentagon_point, angle=0):
    first_line = sd.get_vector(start_point=pentagon_point, angle=0, length=150, width=3)
    first_line.draw(color=colors[color_number])

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 72, length=150, width=3)
    second_line.draw(color=colors[color_number])

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 144, length=150, width=3)
    third_line.draw(color=colors[color_number])

    fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 216, length=150, width=3)
    fourth_line.draw(color=colors[color_number])

    sd.line(start_point=fourth_line.end_point, end_point=pentagon_point, width=3,
            color=colors[color_number])


start_point_hexagon_x = point.x + 150
start_point_hexagon_y = point.y - 150
hexagon_point = sd.get_point(start_point_hexagon_x, start_point_hexagon_y)


def hexagon(hexagon_point, angle=0):
    first_line = sd.get_vector(start_point=hexagon_point, angle=0, length=125, width=3)
    first_line.draw(color=colors[color_number])

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 60, length=125, width=3)
    second_line.draw(color=colors[color_number])

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 120, length=125, width=3)
    third_line.draw(color=colors[color_number])

    fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 180, length=125, width=3)
    fourth_line.draw(color=colors[color_number])

    fifth_line = sd.get_vector(start_point=fourth_line.end_point, angle=angle + 240, length=125, width=3)
    fifth_line.draw(color=colors[color_number])

    sd.line(start_point=fifth_line.end_point, end_point=hexagon_point, width=3, color=colors[color_number])


triangle(triangle_point)
square(square_point)
pentagon(pentagon_point)
hexagon(hexagon_point)

sd.pause()
