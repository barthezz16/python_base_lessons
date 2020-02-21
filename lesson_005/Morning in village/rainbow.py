# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1200, 800)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

x = 1200
y = 400
for color in rainbow_colors:
    x += 5
    start_point = sd.get_point(x, y)
    x1 = x - 700
    y1 = y + 800
    end_point = sd.get_point(x1, y1)
    sd.line(start_point=start_point, end_point=end_point, color=color, width=15)



# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво




#зачет!