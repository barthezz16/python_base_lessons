# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

x_list = []
y_list = []
snowflake_size = []
snowflake = [[x_list], [y_list]]
for i in range(0, 21, 1):
    x_list.append(sd.random_number(25, 1000))
    y_list.append(sd.random_number(800, 821))
    snowflake_size.append(sd.random_number(15, 36))

while True:
    sd.clear_screen()
    point = sd.get_point(x_list[0], y_list[0])
    # TODO Здесь конечно нужно тоже использовать цикл по спискам
    # TODO Лучшей практикой будет for i, y in enumerate(список):
    # TODO Так у вас будет доступ и к индексам (i) и к объектам списка

    # TODO В итоге общий алгоритм следующий
    # TODO циклом проходим по списку со снежинками
    # TODO     получаем точку из текущих координат
    # TODO     рисуем снежинку фоном
    # TODO     меняем координату и получаем новую точку
    # TODO     рисуем снежинку белым цветом

for i in enumerate(snowflake):



# sd.snowflake(center=point, length=12)
# y -= 10
# if y < 50:
#     break
#
# point2 = sd.get_point(x_list[1], y)
# sd.snowflake(center=point2, length=5)
#
# point3 = sd.get_point(x_list[2], y)
# sd.snowflake(center=point3, length=48)
#
# point4 = sd.get_point(x_list[3], y)
# sd.snowflake(center=point4, length=34)
#
# point5 = sd.get_point(x_list[4], y)
# sd.snowflake(center=point5, length=23)
#
# point6 = sd.get_point(x_list[5], y)
# sd.snowflake(center=point6, length=12)
#
# point7 = sd.get_point(x_list[6], y)
# sd.snowflake(center=point7, length=50)
#
# point8 = sd.get_point(x_list[7], y)
# sd.snowflake(center=point8, length=44)
#
# point9 = sd.get_point(x_list[8], y)
# sd.snowflake(center=point9, length=32)
#
# point10 = sd.get_point(x_list[9], y)
# sd.snowflake(center=point10, length=29)
#
# point11 = sd.get_point(x_list[10], y)
# sd.snowflake(center=point11, length=54)
#
# point12 = sd.get_point(x_list[11], y)
# sd.snowflake(center=point12, length=38)
#
# point13 = sd.get_point(x_list[12], y)
# sd.snowflake(center=point13, length=33)
#
# point14 = sd.get_point(x_list[13], y)
# sd.snowflake(center=point14, length=21)
#
# point15 = sd.get_point(x_list[14], y)
# sd.snowflake(center=point15, length=27)
#
# point16 = sd.get_point(x_list[15], y)
# sd.snowflake(center=point16, length=19)
#
# point17 = sd.get_point(x_list[16], y)
# sd.snowflake(center=point17, length=20)
#
# point18 = sd.get_point(x_list[17], y)
# sd.snowflake(center=point18, length=51)
#
# point19 = sd.get_point(x_list[18], y)
# sd.snowflake(center=point19, length=14)
#
# point20 = sd.get_point(x_list[19], y)
# sd.snowflake(center=point20, length=36)

sd.sleep(0.1)
if sd.user_want_exit():
    break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
