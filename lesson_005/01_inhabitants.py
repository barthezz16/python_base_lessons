# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1
import room_2
s = ' и '
print('В комнате room_1 живут:', s.join(room_1.folks))
print('В комнате room_1 живeт:', room_2.folks[0])
#зачет!