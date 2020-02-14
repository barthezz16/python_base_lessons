# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

figures = ('triangle', 'квадрат', 'пятиугольник', 'шестиугольник')
print('Возможные фигуры', '\n', '0 : треугольник', '\n', '1 : квадрат', '\n', '2 : пятиугольник', '\n',
      '3 : шестиугольник')

while True:
    user_input = input("Введите желаемую фигуру ")
    figure_number = int(user_input)
    if figure_number <= len(figures) - 1:
        break
    else:
        print('Введен некорректный номер')

length = 200
point = sd.get_point(100, 100)


def triangle(point, angle=0):
    first_line = sd.get_vector(start_point=point, angle=0, length=200, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 120, length=200, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 240, length=200, width=3)
    third_line.draw()


# triangle(point)


def square(point, angle=0):
    first_line = sd.get_vector(start_point=point, angle=0, length=200, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 90, length=200, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 180, length=200, width=3)
    third_line.draw()

    fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 270, length=200, width=3)
    fourth_line.draw()


# square(point)


def pentagon(point, angle=0):
    first_line = sd.get_vector(start_point=point, angle=0, length=150, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 72, length=150, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 144, length=150, width=3)
    third_line.draw()

    fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 216, length=150, width=3)
    fourth_line.draw()

    fifth_line = sd.get_vector(start_point=fourth_line.end_point, angle=angle + 288, length=150, width=3)
    fifth_line.draw()


# pentagon(point)


def hexagon(point, angle=0):
    first_line = sd.get_vector(start_point=point, angle=0, length=125, width=3)
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


# hexagon(point)

if user_input == 0:
    triangle(point)
elif user_input == 1:
    square(point)
elif user_input == 2:
    pentagon(point)
elif user_input == 3:
    hexagon(point)

print(user_input)

sd.pause()
