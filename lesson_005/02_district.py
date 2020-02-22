# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from district.central_street.house1.room1 import folks as folks_cs_1_1
from district.central_street.house1.room2 import folks as folks_cs_1_2
from district.central_street.house2.room1 import folks as folks_cs_2_1
from district.central_street.house2.room2 import folks as folks_cs_2_2
from district.soviet_street.house1.room1 import folks as folks_ss_1_1
from district.soviet_street.house1.room2 import folks as folks_ss_1_2
from district.soviet_street.house2.room1 import folks as folks_ss_2_1
from district.soviet_street.house2.room2 import folks as folks_ss_2_2

s = ', '

# print('На районе живут ...')
# print(s.join(folks_cs_1_1))
# print(s.join(folks_cs_1_2))
# print('В первой комнате, во втором доме, на центральной улице никто не живет')
# print(s.join(folks_cs_2_2))
# print(s.join(folks_ss_1_1))
# print(s.join(folks_ss_1_2))
# print(s.join(folks_ss_2_1))
# print(s.join(folks_ss_2_2))

citizens_list = folks_ss_1_1 + folks_cs_1_2 + folks_cs_1_2 + folks_cs_2_2 + folks_ss_1_1 + folks_ss_1_2 \
                + folks_ss_2_1 + folks_ss_2_2

print(s.join(citizens_list))
