# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (1200, 800)
x = 300
y = 0
row = 0

# for y in range(0, 800, 50):
#     if row % 2 == 0:
#         x = -50
#     else:
#         x = 0
#     row += 1
#     for _ in range(0, 800, 100):
#         left_bottom = sd.get_point(x, y)
#         x += 100
#         x1 = x + 100
#         y1 = y + 50
#         right_top = sd.get_point(x1, y1)
#         sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=2)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# Вариант попроще:

for row, y in enumerate(range(0, 200, 25)):
    x0 = 350 if row % 2 == 0 else 325
    for x in range(x0, 700, 50):
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + 50, y + 25)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=2)
left_bottom_sr_x = 325
left_bottom_sr_y = 0
left_bottom_sr = sd.get_point(left_bottom_sr_x, left_bottom_sr_y)
right_top_sr_x = 725
right_top_sr_y = 200
right_top_sr = sd.get_point(right_top_sr_x, right_top_sr_y)
sd.rectangle(left_bottom=left_bottom_sr, right_top=right_top_sr, width=2)
left_bottom_sq_x = 425
left_bottom_sq_y = 25
left_bottom_sq = sd.get_point(left_bottom_sq_x, left_bottom_sq_y)
sd.square(left_bottom=left_bottom_sq, side=150, color=sd.background_color, width=0)
sd.square(left_bottom=left_bottom_sq, side=150, width=3)
#зачет!