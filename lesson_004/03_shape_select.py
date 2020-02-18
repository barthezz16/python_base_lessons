# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def triangle(point, angle=0):
    first_line = sd.get_vector(start_point=point, angle=0, length=200, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 120, length=200, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 240, length=200, width=3)
    third_line.draw()


def square(point, angle=0):
    first_line = sd.get_vector(start_point=point, angle=0, length=200, width=3)
    first_line.draw()

    second_line = sd.get_vector(start_point=first_line.end_point, angle=angle + 90, length=200, width=3)
    second_line.draw()

    third_line = sd.get_vector(start_point=second_line.end_point, angle=angle + 180, length=200, width=3)
    third_line.draw()

    fourth_line = sd.get_vector(start_point=third_line.end_point, angle=angle + 270, length=200, width=3)
    fourth_line.draw()


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


length = 200
point = sd.get_point(100, 100)
figures = {'0': triangle, '1': square, '2': pentagon, '3': hexagon}
print('Возможные фигуры', '\n', '0 : треугольник', '\n', '1 : квадрат', '\n', '2 : пятиугольник', '\n',
      '3 : шестиугольник')

while True:
    user_input = input("Введите желаемую фигуру ")
    if user_input in figures:
        break
    else:
        print('Введен некорректный номер')

func = figures[user_input]
func(point)
sd.pause()
