# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

x = 50
y = 50
for color in rainbow_colors:
    x += 5
    start_point = sd.get_point(x, y)
    x1 = x + 300
    y1 = y + 400
    end_point = sd.get_point(x1, y1)
    sd.line(start_point=start_point, end_point=end_point, color=color, width=4)

sd.pause()

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


sd.pause()

#зачет!