# используется для сортировки
from operator import itemgetter
from ds import Cd
from ds import Lib
from ds import LibCd

# Отделы
cdc = [
    Cd(1, 'Группа крови', 'Цой', 200, 1),
    Cd(2, 'Туман', 'Сектор газа', 300, 1),
    Cd(3, 'Кукла колдуна', 'Сектор газа', 442, 1),
    Cd(4, 'Земля у дома', 'Земляне', 126, 1),
    Cd(5, 'Искала', 'Земфира', 672, 2),
    Cd(6, 'Хочешь?', 'Земфира', 456, 2),
    Cd(7, 'Ромашки', 'Земфира', 300, 2),
    Cd(9, 'Гранитный камушек', 'Божья коровка', 228, 2),
    Cd(11, 'Shake it off', 'Taylor Swift', 546, 3),
    Cd(14, 'Complicated', 'Avril Lavigne', 219, 3),
    Cd(10, 'Poker Face', 'Lady Gaga', 341, 3),
    Cd(8, 'Мы Ранетки', 'Ранетки', 145, 4),
    Cd(12, 'Зима', 'Ранетки', 765, 4),
    Cd(13, 'Ангелы', 'Ранетки', 99, 4)

]

# Сотрудники
libs = [
    Lib(1, 'Диски 80-ых'),
    Lib(2, 'Все о Земфире'),
    Lib(3, 'Иностранная попса'),
    Lib(4, 'Диски для девочек')

]

libs_cdc = [
    LibCd(1, 1),
    LibCd(2, 1),
    LibCd(3, 1),
    LibCd(4, 1),
    LibCd(5, 2),
    LibCd(6, 2),
    LibCd(7, 2),
    LibCd(8, 4),
    LibCd(9, 2),
    LibCd(10, 3),
    LibCd(11, 3),
    LibCd(12, 4),
    LibCd(13, 4),
    LibCd(14, 3),

]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(c.song, c.author, c.price, l.name)
                   for l in libs
                   for c in cdc
                   if c.lib_id == l.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, lc.lib_id, lc.cd_id)
                         for l in libs
                         for lc in libs_cdc
                         if l.id == lc.lib_id]

    many_to_many = [(c.song, c.author, c.price, lib_name)
                    for lib_name, lib_id, cd_id in many_to_many_temp
                    for c in cdc if c.id == cd_id]

    print('Задание Д1')
    res_11 = [(cd[1], cd[3]) for cd in one_to_many if cd[1][-1] == 'a' or cd[1][-1] == 'а']
    for i in res_11:
        print(*i, sep=' --- ')

    print('\nЗадание Д2')
    res_12_unsorted = []
    # Перебираем все библиотеки
    for l in libs:
        # Список дисков библиотеки
        l_cds = list(filter(lambda i: i[3] == l.name, one_to_many))
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

    print('\nЗадание Д3')
    res_13 = {}
    # Перебираем все библиотеки
    for l in libs:
        if l.name[0] == 'Д':
            # Список дисков библиотеки
            l_cds = list(filter(lambda i: i[3] == l.name, many_to_many))
            # Только название песни
            l_cdc_names = [x for x, _, _, _ in l_cds]
            # Добавляем результат в словарь
            # ключ - библиотека, значение - список дисков
            res_13[l.name] = l_cdc_names

    for key, value in res_13.items():
        print(key, end=':\n')
        for v in value:
            print('\t', v)


if __name__ == '__main__':
    main()
