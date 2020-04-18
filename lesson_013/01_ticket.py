# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


def make_ticket(fio, from_, to, date):
    template = "ticket_template.png"
    image = Image.open(template)
    draw = ImageDraw.Draw(image)
    font_path = os.path.join("Calibri.ttf")
    font = ImageFont.truetype(font_path, size=20)
    x = 45
    y = 125
    message = f"{fio}"
    draw.text((x, y), message, font=font, fill=ImageColor.colormap['black'])
    message = f"{from_}"
    draw.text((x, y + 69), message, font=font, fill=ImageColor.colormap['black'])
    message = f"{to}"
    draw.text((x, y + 135), message, font=font, fill=ImageColor.colormap['black'])
    message = f"{date}"
    draw.text((x + 242, y + 135), message, font=font, fill=ImageColor.colormap['black'])
    out_path = 'ticket.png'
    image.save(out_path)
    print(f'Post card saved as {out_path}')


make_ticket(fio='Sorokin Iurii', from_='Moscow', to='New York', date='4.18.2020')

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
