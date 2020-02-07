# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей


educational_grant, expenses = 10000, 12000
difference = 0
inflation = 0
need_help = 0
i = 0
while i < 10:
    i += 1
    difference = expenses - educational_grant
    inflation = expenses / 100 * 3
    expenses = expenses + inflation
    need_help = need_help + difference

else:
    print('Студенту надо попросить', need_help.__round__(2), 'рублей')


