# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
import numpy

import math


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.i, self.a, = 2, 2
        self.n = n

    def __iter__(self):
        self.i, self.a = 2, 2
        self.prime_list = []
        return self

    def __next__(self):
        while True:
            if self.i > self.n:
                raise StopIteration('число(i) больше n')
            for self.a in self.prime_list:
                if self.i % self.a == 0:
                    break
            else:
                self.prime_list.append(self.i)
                return self.i
            self.i += 1


prime_number_iterator = PrimeNumbers(n=10000)


# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

def prime_numbers_generator(n):
    prime_list = set()
    for i in range(2, n + 1):
        if i not in prime_list:
            x, y, z = str(i), str(i), str(i)
            x = happy(x)
            y = poli(y)
            z = multiplication(z)
            yield i, x, y, z
            prime_list.update(range(i * i, n + 1, i))




def happy(number):
    number_str = str(number)
    number_list = [int(x) for x in list(str(number))]
    x = math.trunc(len(number_str) * 0.5)
    if len(number_str) >= 2 and sum(number_list[:x]) == sum(number_list[-x::]):
        return '- счастливое'
    else:
        return ''


def poli(number):
    number = str(number)
    if number == number[::-1]:
        return '- полиндромное'
    else:
        return ''


def multiplication(number):
    number_str = str(number)
    number_list = [int(x) for x in list(str(number))]
    x = math.trunc(len(number_str) * 0.5)
    if len(number_str) >= 2 and numpy.prod(number_list[:x]) == numpy.prod(number_list[-x::]):
        return '- произведение первых числе равно произведению последних'
    else:
        return ''


for number in prime_numbers_generator(n=100000):
    print(number)

# for number in prime_numbers_generator(n=100000):
#     # result_happy = happy(number)
#     # result_poli = poli(number)
#     # result_mul = multiplication(number)
#     # print(number, result_happy, result_poli, result_mul)
#     print(number, happy(number), poli(number), multiplication(number))


# for number_iter, number_gen in zip(prime_number_iterator, prime_numbers_generator(n=10000)):
#     print(number_iter == number_gen)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
# Пример:
class PrimeNumbers:
    def __init__(self, n, list_of_filters):
        self.i, self.a, = 2, 2
        self.n = n
        self.filters = list_of_filters

    def __iter__(self):
        self.i, self.a = 2, 2
        self.prime_list = []
        return self

    def __next__(self):
        while True:
            if self.i > self.n:
                raise StopIteration('число(i) больше n')
            for self.a in self.prime_list:
                if self.i % self.a == 0:
                    break
            else:
                self.prime_list.append(self.i)
                result = str(self.i)
                for func in self.filters:
                    result += func(self.i)
                return result
            self.i += 1


filters = [poli, happy, multiplication]
prime_number_iterator = PrimeNumbers(n=10000, list_of_filters=filters)
for i in prime_number_iterator:
    print(i)

#зачет!