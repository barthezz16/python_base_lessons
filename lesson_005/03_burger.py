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

from my_burger import my_burger_recipe
# TODO Идея хороша для сокращения кода, однако тут важно было попрактиковаться в импорте множества функций
# TODO Поэтому нужно сделать по простенькой функции на каждый ингридиент и имортировать их при помощи
# TODO from ... import func1, func2, func3 и тд

# TODO + длинные строки оставлять нельзя
ingredients = [' - карамелизованные булочки', ' - два рубленых бифштекса', ' - огурчика', ' - помидорчика', ' - майонеза', ' - кетчупа', ' - сыра']
my_burger_recipe(ingredients)

