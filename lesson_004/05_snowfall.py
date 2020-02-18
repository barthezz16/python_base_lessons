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
for i in range(21):
    x_list.append(sd.random_number(25, 1000))
    y_list.append(sd.random_number(600, 621))
    snowflake_size.append(sd.random_number(15, 36))

while True:
    sd.clear_screen()
    for i, y in enumerate(y_list):
        for i, x in enumerate(x_list):  # TODO вложенный цикл не нужен
            # TODO нам достаточно пройти циклом по одному списку, тк мы в любом случае используем "i"
            # TODO Для доступа к элементам сразу всех нужных списков
            point = sd.get_point(x, y)  # TODO тут можно использовать x_list[i] и y_list[i]
            sd.snowflake(center=point, length=50)  # TODO Кстати тут вместо длины можно использовать элементы из списка
            # TODO snoWflake_size который
            y_list[i] -= 5
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
