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
for i in range(10):
    x_list.append(sd.random_number(25, 400))
    y_list.append(sd.random_number(750, 880))
    snowflake_size.append(sd.random_number(15, 36))

while True:
    for i, y in enumerate(y_list):
        sd.start_drawing()
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.COLOR_WHITE)  # TODO здесь эта строка лишняя
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.background_color)
        y_list[i] -= 5
        # TODO А тут надо обновить точку point, чтобы в ней была измененная координата
        sd.snowflake(center=point, length=snowflake_size[i], color=sd.COLOR_WHITE)
        # TODO + если хотите, чтобы анимация продолжалась, надо придумать что делать с упавшими снежинками
        # TODO по координате y смотреть - упала ли снежинка и дальше можно например запустить её в полет
        # TODO Или не менять для таких снежинок координаты, чтобы они замерли в сугробе.
    sd.finish_drawing()
    sd.sleep(.05)
    if sd.user_want_exit() or i == 100:  # TODO "i" в данном случае больше 100 не станет никогда
        # TODO тк "i" по сути считает итерации цикла for, каждый раз начиная с 0 и заканчивая на 10
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