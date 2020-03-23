# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.clean = 0
        self.cats_food = 50

    def __str__(self):
        return 'В доме еды осталось {}, в доме кошачьей еды осталось {}, денег осталось {}, грязи в доме {}'.format(
            self.food, self.cats_food, self.money, self.clean)


class Human:

    def __init__(self, name):
        self.name = name
        self.happiness = 100
        self.fullness = 30
        self.house = None
        self.total_food = 0
        self.total_money = 0
        self.total_furs = 0

    def __str__(self):
        return 'Я - {}, сытость {}, счастья {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        portion_size = randint(15, 30)
        if portion_size > self.house.food:
            portion_size = self.house.food
        else:
            portion_size = portion_size
        if self.house.food >= portion_size:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.fullness += portion_size
            self.total_food += portion_size
            self.house.food -= portion_size
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def stroke_cat(self):
        cprint('{} гладил кота'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 10


class Husband(Human):

    def __str__(self):
        return 'Я - {}, сытость - {}, счастья - {}'.format(self.name, self.fullness, self.happiness)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.happiness <= 10:
            cprint('{} умер от депрессии'.format(self.name), color='red')
            return
        if self.fullness <= 20:
            self.eat()
        elif self.happiness <= 40:
            self.stroke_cat()
        elif self.house.money > 300 and self.happiness < 40:
            self.gaming()
        else:
            self.work()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10
        self.happiness -= 10
        self.total_money += 150

    def gaming(self):
        cprint('{} играл в WoT'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20

    def go_to_the_house(self, house):
        self.house = house


class Wife(Human):

    def __str__(self):
        return 'Я - {}, сытость {}, счастья {}'.format(self.name, self.fullness, self.happiness)

    def act(self):
        dice = randint(1, 5)
        self.house.clean += 5
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.happiness <= 10:
            cprint('{} умер от депрессии'.format(self.name), color='red')
            return
        if self.house.clean >= 90:
            self.happiness -= 10
        if self.house.food < 20 or self.house.cats_food < 10 and self.house.money != 0:
            self.shopping()
        elif self.fullness <= 20:
            self.eat()
        elif self.house.clean > 80:
            self.clean_house()
        elif self.happiness <= 40:
            self.stroke_cat()
        elif self.house.money > 400 and self.happiness <= 40:
            self.buy_fur_coat()
        elif dice == 1:
            self.buy_fur_coat()
        else:
            cprint('{} скучает'.format(self.name), color='magenta')

    def shopping(self):
        food_amount = randint(50, 100)
        cat_food_amount = randint(10, 25)
        self.fullness -= 10
        if self.house.money >= food_amount + cat_food_amount:
            cprint('{} сходила в магазин за едой для всех'.format(self.name), color='magenta')
            self.house.money -= food_amount
            self.house.food += food_amount
            self.house.cats_food += cat_food_amount
            self.happiness -= 10
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        if self.house.money >= 350:
            cprint('{} купила очередную шубу'.format(self.name), color='magenta')
            self.house.money -= 350
            self.happiness += 60
            self.fullness -= 10
            self.total_furs += 1

    def clean_house(self):
        cprint('{} убралась дома'.format(self.name), color='blue')
        self.house.clean -= 80
        self.fullness -= 10
        self.happiness -= 10

    def go_to_the_house(self, house):
        self.house = house


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# serge.go_to_the_house(house=home)
# masha.go_to_the_house(house=home)
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
#
# cprint('{} съел еды - {}'.format(serge.name, serge.total_food), color='yellow')
# cprint('{} заработал денег - {}'.format(serge.name, serge.total_money), color='yellow')
# cprint('{} съела еды - {}'.format(masha.name, masha.total_food), color='yellow')
# cprint('{} купила шуб - {}'.format(masha.name, masha.total_furs), color='yellow')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat_total_food = 0
        pass

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(
            self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.soil()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        cats_portion_size = randint(2, 10)
        if cats_portion_size > self.house.cats_food:
            cats_portion_size = self.house.cats_food
        else:
            cats_portion_size = cats_portion_size
        if self.house.cats_food >= cats_portion_size:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.fullness += cats_portion_size*2
            self.cat_total_food += cats_portion_size
            self.house.cats_food -= cats_portion_size
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} спал весь день'.format(self.name), color='blue')
        self.fullness -= 10

    def soil(self):
        cprint('{} подрал обои'.format(self.name), color='blue')
        self.house.clean += 5
        self.fullness -= 10

    def go_to_the_house(self, house):
        self.house = house


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
# kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')
serge.go_to_the_house(house=home)
masha.go_to_the_house(house=home)
murzik.go_to_the_house(house=home)



for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    # kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    # cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')


cprint('{} съел еды - {}'.format(serge.name, serge.total_food), color='yellow')
cprint('{} заработал денег - {}'.format(serge.name, serge.total_money), color='yellow')
cprint('{} съела еды - {}'.format(masha.name, masha.total_food), color='yellow')
cprint('{} купила шуб - {}'.format(masha.name, masha.total_furs), color='yellow')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
