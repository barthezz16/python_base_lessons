#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

my_family = ['Mother', 'Father', 'Brother']
my_family_height = [
    ['Zina', 164],
    ['Yura', 179],
    ['Igor', 186]
]
print('Рост отца - ' + str(my_family_height[1][1]) + " см")
my_family_total = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print('Общий рост моей семьи -', my_family_total, 'см')
