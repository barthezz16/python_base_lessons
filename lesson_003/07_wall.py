# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

x = 0
y = 0
row = 0

for y in range(0, 800, 50):
    if row % 2 == 0:
        x = -50
    else:
        x = 0
    row += 1
    for _ in range(0, 800, 100):
        left_bottom = sd.get_point(x, y)
        x += 100
        x1 = x + 100
        y1 = y + 50
        right_top = sd.get_point(x1, y1)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=2)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


sd.pause()
