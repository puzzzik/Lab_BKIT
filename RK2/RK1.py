# -*- coding: utf-8 -*-
# используется для сортировки
from operator import itemgetter


class RK1:
    def __init__(self, cdc, libs, libs_cdc):
        self.cdc = cdc
        self.libs = libs
        self.libs_cdc = libs_cdc
        self.one_to_many = [(c.song, c.author, c.price, l.name)
                       for l in libs
                       for c in cdc
                       if c.lib_id == l.id]

        # Соединение данных многие-ко-многим
        self.many_to_many_temp = [(l.name, lc.lib_id, lc.cd_id)
                             for l in libs
                             for lc in libs_cdc
                             if l.id == lc.lib_id]

        self.many_to_many = [(c.song, c.author, c.price, lib_name)
                        for lib_name, lib_id, cd_id in self.many_to_many_temp
                        for c in cdc if c.id == cd_id]

    def N1(self):
        print('Задание Д1')
        res_11 = [(cd[1], cd[3]) for cd in self.one_to_many if cd[1][-1] == 'a' or cd[1][-1] == 'а']
        for i in res_11:
            print(*i, sep=' --- ')
        return res_11

    def N2(self):
        print('\nЗадание Д2')
        res_12_unsorted = []
        # Перебираем все библиотеки
        for l in self.libs:
            # Список дисков библиотеки
            l_cds = list(filter(lambda i: i[3] == l.name, self.one_to_many))
            # Если библиотека не пустая
            if len(l_cds) > 0:
                # Цены дисков библиотеки
                l_prices = [price for _, _, price, _ in l_cds]
                # Cредняя цена дисков библиотеки
                l_prices_av = sum(l_prices) / len(l_prices)
                res_12_unsorted.append((l.name, l_prices_av))

        # Сортировка по средней цене
        res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
        for i in res_12:
            print(*i, sep=' --- ')
        return res_12

    def N3(self):
        print('\nЗадание Д3')
        res_13 = {}
        # Перебираем все библиотеки
        for l in self.libs:
            if l.name[0] == 'Д':
                # Список дисков библиотеки
                l_cds = list(filter(lambda i: i[3] == l.name, self.many_to_many))
                # Только название песни
                l_cdc_names = [x for x, _, _, _ in l_cds]
                # Добавляем результат в словарь
                # ключ - библиотека, значение - список дисков
                res_13[l.name] = l_cdc_names

        for key, value in res_13.items():
            print(key, end=':\n')
            for v in value:
                print('\t', v)
        return res_13