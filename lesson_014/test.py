def analyzing_result(result):
    global analized_res, total
    analized_res = {}
    total = 0
    for _ in result:
        for i, k in enumerate(zip(result.replace('X', 'X-')[0::2], result.replace('X', 'X-')[1::2]), start=1):
            analized_res[i] = k
    print(analized_res)
    for k, v in analized_res.items():
        print(v)


#  Я бы наверное передавал фрэйм в отдельную функцию, из которой возвращал
#  Бы результатом другой фрейм. Новый фрейм добавлял бы в измененный список.
#  Это бы упростило слегка структуру алгоритма.
#  А на счёт изменений двух знаков в фрейме - можно использовать цикл по фрейму (2 итерации)
#  может быть на совсем верно, но хочу все значения в цифры перевести, мне кажется так лешче будет...
#  Но если вы переведете всё в числа, то как вы будете начислять бонусные очки?
#  Тем более, что числа будут строками, так ведь?
# {1: 10, 2: ('3', '4'), 3: (0, 10), 4: ('1', '7'), 5: ('4', '4'), 6: 10, 7: 10, 8: ('2', '3'), 9: (0, 0), 10: ('4', 6)}
#   Максим, тут то и проблема, это один из тех вариантов где даже не знаю с чего подойти, сначала думал перевести все
#   в цифры, как выше, и потом перепести все в список, но потому уперся в то, что нет идей как это потом
#   на фреймы разбить.
#   Второй вариант был попробовать каждый фрейм отдельно обработать как раньше, но как в случае страйка прибавить
#   очки из следующего фрейма тоже не понятно пока... Вот так уже 2 день и сижу прижумать не могу...
#    Ваш вариант:
#                   "Я бы наверное передавал фрэйм в отдельную функцию, из которой возвращал
#                   Бы результатом другой фрейм. Новый фрейм добавлял бы в измененный список.
#                   Это бы упростило слегка структуру алгоритма."
#  я вообще не понял...
#  ступор наверно в том, что я не пойму как проходясь циклом по списку, имея в данный момент какоето
#  значение, проверить его, например на страйк, и случае совпадения взять следующие значения и прибавить их
# TODO Можно сделать функцию, которая будет вызываться при нахождении 'X' или '/'
# TODO Она будет брать 1-2 следующих броска, доступ к ним можно получить по фрейму
# TODO Например нашли в первом броске "X"
# TODO Запустили функцию(ключ='1', количество_доп_бросков=2)
# TODO Берется фрейм '2' - бросок 3 + бросок 4 - возвращается 7 очков, которые плюсуются к первому фрейму
# TODO А дальше обработка граничных условий. Если в броске встречен символ - не число, то проверяем какой именно символ
# TODO Если / - значит добавляем 10 очков. "-" - это ноль очков. "Х" - добавляем 10 следующий бросок, если нужен,
# TODO берем из следующего фрейма (если следующий фрейм есть).
result = 'X34-/1744XX23--4/'
analyzing_result(result)
