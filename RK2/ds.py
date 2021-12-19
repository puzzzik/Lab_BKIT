class Cd:
    """CD-диск"""

    def __init__(self, id, song, author, price, lib_id):
        self.id = id
        self.song = song
        self.author = author
        self.price = price
        self.lib_id = lib_id


class Lib:
    """Библиотека"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class LibCd:
    """
    'Диск из библиотеки' для реализации
    связи многие-ко-многим
    """

    def __init__(self, cd_id, lib_id):
        self.cd_id = cd_id
        self.lib_id = lib_id

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