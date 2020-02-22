# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

# from my_burger import my_burger_recipe

from my_burger import first_item, second_item, third_item, fourth_item, fifth_item


# ingredients = [' - карамелизованные булочки', ' - два рубленых бифштекса', ' - огурчика', ' - помидорчика',
#                ' - майонеза', ' - кетчупа', ' - сыра']
# my_burger_recipe(ingredients)

ingredient_1 = '- карамелизованные булочки'
ingredient_2 = '- два рубленых бифштекса'
ingredient_3 = '- кетчупа'
ingredient_4 = '- майонеза'
ingredient_5 = '- сыра'

first_item(ingredient_1)
second_item(ingredient_2)
third_item(ingredient_3)
fourth_item(ingredient_4)
fifth_item(ingredient_5)
