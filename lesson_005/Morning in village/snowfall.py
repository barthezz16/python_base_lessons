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
for i in range(20):
    x_list.append(sd.random_number(25, 350))
    y_list.append(sd.random_number(800, 880))
    snowflake_size.append(sd.random_number(15, 36))

while True:
    sd.start_drawing()
    for i, y in enumerate(y_list):
        point = sd.get_point(x_list[i], y_list[i])
        print(sd.background_color, sd.COLOR_WHITE)  # TODO Повозиться пришлось с этой причиной :)
        # TODO А была она в том, что фоновый цвет при запуске из другого модуля имеет белый цвет по какой-то причине
        # TODO И поэтому снежинки просто два раза рисовались вместо закрашивания
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.background_color)
        y_list[i] -= 5
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(.05)
    if sd.user_want_exit() or y_list[i] <= 100:
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
#зачет!