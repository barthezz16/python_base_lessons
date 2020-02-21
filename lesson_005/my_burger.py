ingredients = [' - булочки', ' - огурчика', ' - помидорчика', ' - майонеза', ' - сыра']


def my_burger_recipe(ingredients):
    for item in ingredients:
        print('А теперь добавим', item)


if __name__ == '__main__':
    my_burger_recipe(ingredients)
