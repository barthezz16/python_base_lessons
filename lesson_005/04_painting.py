# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from snowfall import snowfall_draw as snow
from wall import wall_draw as wall
from tree import branch as tree_1
from tree_2 import branch as tree_2
from rainbow_round import rainbow_round_draw as rainbow
from sun import sun_draw as sun
from smile import smile_draw as smile
from roof import roof_draw as roof
point_tree_1 = sd.get_point(800, 0)
angle_tree_1 = 90
length_tree_1 = 100
point_tree_2 = sd.get_point(900, 0)
angle_tree_2 = 90
length_tree_2 = 50
point_sun = sd.get_point(100, 650)
point_smile = sd.get_point(500, 100)
snow()
wall()
roof()
tree_1(point=point_tree_1, angle=angle_tree_1, length=length_tree_1)
tree_2(point=point_tree_2, angle=angle_tree_2, length=length_tree_2)
rainbow()
sun(point=point_sun)
smile(point=point_smile)

sd.pause()
# TODO сейчас проде все получилось, но есть вопрос, как сделать так, чтобы все функции запустились одновременно?



# функция_1()
# функция_2()
# функция_3()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
