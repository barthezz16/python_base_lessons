# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой себе и котам'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
            self.house.cats_food += 60
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def take_cat(self, cat):
        self.cat = cat
        self.pets = []
        self.pets.append(cat)
        cat.house = self.house
        cprint('{} подобрал кота {}'.format(self.name, self.cat.name), color='cyan')

    def make_clean(self):
        cprint('{} убрался дома'.format(self.name), color='blue')
        self.house.clean -= 80
        self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 5)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cats_food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.clean > 80:
            self.make_clean()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.cats_food = 0
        self.clean = 0

    def __str__(self):
        return 'В доме еды осталось {}, в доме кошачьей еды осталось {}, денег осталось {}, грязи в доме {}'.format(
            self.food, self.cats_food, self.money, self.clean)


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cats_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 15
            self.house.cats_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} спал весь день'.format(self.name), color='blue')
        self.fullness -= 10

    def tear_the_wallpaper(self):
        cprint('{} подрал обои'.format(self.name), color='blue')
        self.house.clean += 20
        self.fullness -= 5

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} теперь живет с Васей'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.tear_the_wallpaper()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()


my_sweet_home = House()
vasya = Man(name='Вася')
tom = Cat(name='Том')
murzik = Cat(name='Мурзик')
murka = Cat(name='Мурка')
vasya.go_to_the_house(house=my_sweet_home)
vasya.take_cat(tom)
vasya.take_cat(murzik)
vasya.take_cat(murka)
tom.go_to_the_house(house=my_sweet_home)
murzik.go_to_the_house(house=my_sweet_home)
murka.go_to_the_house(house=my_sweet_home)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    vasya.act()
    tom.act()
    murzik.act()
    murka.act()
    print(vasya)
    print(tom)
    print(murzik)
    print(murka)
    print('--- в конце дня ---')
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
