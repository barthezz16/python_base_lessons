# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO Так конечно делать не стоит, надо использовать цикл, чтобы избежать от дублирования кода
sd.resolution = (1000, 500)
# TODO В цикле можно добавлять координатам +5, а потом делать из них точки и по точкам рисовать линию
# TODO условно x1 += 5, y1 += 5, x2 и y2 (которые представляют верхнюю точку) можно не увеличивать
# TODO А просто получать из x1 и y1
# TODO Например нижняя точка (x1, y1) - верхняя тогда - (x1 + 300, y1 + 400)
x1 = sd.get_point(50, 50)
x2 = sd.get_point(55, 50)
x3 = sd.get_point(60, 50)
x4 = sd.get_point(65, 50)
x5 = sd.get_point(70, 50)
x6 = sd.get_point(75, 50)
x7 = sd.get_point(80, 50)
y1 = sd.get_point(350, 450)
y2 = sd.get_point(355, 450)
y3 = sd.get_point(360, 450)
y4 = sd.get_point(365, 450)
y5 = sd.get_point(370, 450)
y6 = sd.get_point(375, 450)
y7 = sd.get_point(380, 450)
sd.line(start_point=x1, end_point=y1, color=sd.COLOR_RED, width=4)
sd.line(start_point=x2, end_point=y2, color=sd.COLOR_ORANGE, width=4)
sd.line(start_point=x3, end_point=y3, color=sd.COLOR_YELLOW, width=4)
sd.line(start_point=x4, end_point=y4, color=sd.COLOR_GREEN, width=4)
sd.line(start_point=x5, end_point=y5, color=sd.COLOR_CYAN, width=4)
sd.line(start_point=x6, end_point=y6, color=sd.COLOR_BLUE, width=4)
sd.line(start_point=x7, end_point=y7, color=sd.COLOR_PURPLE, width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


sd.pause()
