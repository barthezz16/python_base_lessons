# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя ни одной из операций деления: ни деления с плавающей точкой /, ни целочисленного деления //
# и взятия остатка %
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 9, 3
a_temp = a
count = 0
while a_temp >= b:
    count += 1
    a_temp -= b
else:
    print('Целочисленное деление', a, 'на', b, 'дает', count)

#зачет!