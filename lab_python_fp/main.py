# -*- coding: utf-8 -*-

import json
import sys
# Сделаем другие необходимые импорты
from gen_random import gen_random
from cm_timer import cm_timer_1
from field import field
from print_result import print_result
from unique import Unique

path = 'data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return list(sorted([el for el in Unique(field(arg, 'job-name'), ignore_case=True)]))


@print_result
def f2(arg):
    #return list(filter(lambda x: x.find('программист') == 0, arg))
    return list(filter(lambda x: x.startswith('Программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    pay = list(gen_random(len(arg), 100000, 200000))
    strs = ['зарплата {} руб.'.format(i) for i in pay]
    return list(zip(arg, strs))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))