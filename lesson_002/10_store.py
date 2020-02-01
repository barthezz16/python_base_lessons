#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
##lamps_item = store[lamp_code][0]
# lamps_quantity = lamps_item['quantity']
# lamps_price = lamps_item['price']
# lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

chair_code = goods['Стул']
chair_item_100 = store[chair_code][0]
chair_item_95 = store[chair_code][1]
chair_item_97 = store[chair_code][2]
chair_quantity_100 = chair_item_100['quantity']
chair_quantity_95 = chair_item_95['quantity']
chair_quantity_97 = chair_item_97['quantity']
chair_quantity_total = chair_quantity_100 + chair_quantity_97 + chair_quantity_95
chair_price_100 = chair_item_100['price']
chair_price_95 = chair_item_95['price']
chair_price_97 = chair_item_97['price']
chair_cost = (chair_quantity_100 * chair_price_100
              + chair_price_95 * chair_quantity_95
              + chair_quantity_97 * chair_price_97)
print('Стул -', chair_quantity_total, 'шт, стоимость', chair_cost, 'руб')

table_code = goods['Стол']
table_item_510 = store[table_code][0]
table_item_520 = store[table_code][1]
table_quantity_510 = table_item_510['quantity']
table_quantity_520 = table_item_520['quantity']
table_quantity_total = table_quantity_510 + table_quantity_520
table_price_510 = table_item_510['price']
table_price_520 = table_item_520['price']
table_cost = table_quantity_510 * table_price_510 + table_quantity_520 * table_price_520
print('Стол -', table_quantity_total, 'шт, стоимость', table_cost, 'руб')

sofa_code = goods['Диван']
sofa_item_1200 = store[sofa_code][0]
sofa_item_1150 = store[sofa_code][1]
sofa_quantity_1200 = sofa_item_1200['quantity']
sofa_quantity_1150 = sofa_item_1150['quantity']
sofa_quantity_total = sofa_quantity_1200 + sofa_quantity_1150
sofa_price_1200 = sofa_item_1200['price']
sofa_price_1150 = sofa_item_1150['price']
sofa_cost = sofa_quantity_1200 * sofa_price_1200 + sofa_quantity_1150 * sofa_price_1150
print('Диван -', sofa_quantity_total, 'шт, стоимость', sofa_cost, 'руб')

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################


#зачет!