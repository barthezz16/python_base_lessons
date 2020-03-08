# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 800)

x_list = []
y_list = []
index_list = []
snowflake_size = []


def snowflake_creating(snowflake_count):
    global x_list, y_list, snowflake_size
    x_list = []
    y_list = []
    snowflake_size = []
    for i in range(snowflake_count):
        x_list.append(sd.random_number(25, 1000))
        y_list.append(sd.random_number(100, 780))
        snowflake_size.append(sd.random_number(15, 35))


def snowflake_color(color=sd.COLOR_WHITE):
    global x_list, y_list
    for i, y in enumerate(y_list):
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=snowflake_size[i], color=color)


def snowflake_deleting():
    for i, y in enumerate(y_list):
        if y < 20:
            index_list.append(i)
    return index_list



def move_snowflake(x_position=3, y_position=5):
    for i, y in enumerate(y_list):
        x_list[i] -= sd.random_number(-x_position, x_position)
        y_list[i] -= y_position

