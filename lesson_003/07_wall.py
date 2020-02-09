# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

left_bottom = sd.get_point(0, 0)
right_top = sd.get_point(100, 50)
for y in range(0, 800, 50):
    for x in range(0, 800, 100):
        left_bottom = sd.get_point(x, y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=2)

# нарисовал но не понял, как смещать новый ряд на 50 пикселей.


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for



sd.pause()
