import unittest
from RK1 import RK1
from ds import Cd
from ds import Lib
from ds import LibCd


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
res_1 = [('Сектор газа', 'Диски 80-ых'),
         ('Сектор газа', 'Диски 80-ых'),
         ('Земфира', 'Все о Земфире'),
         ('Земфира', 'Все о Земфире'),
         ('Земфира', 'Все о Земфире'),
         ('Божья коровка', 'Все о Земфире'),
         ('Lady Gaga', 'Иностранная попса')
         ]
res_2 = [
    ('Все о Земфире', 414.0),
    ('Иностранная попса', 368.6666666666667),
    ('Диски для девочек', 336.3333333333333),
    ('Диски 80-ых', 267.0)
]

res_3 = {
    'Диски 80-ых':
        [
            'Группа крови',
            'Туман',
            'Кукла колдуна',
            'Земля у дома'
        ],
    'Диски для девочек':
        [
            'Мы Ранетки',
            'Зима',
            'Ангелы'
        ]
}

class MyTestCase(unittest.TestCase):
    def test_n1(self):
        rk = RK1(cdc, libs, libs_cdc)
        self.assertEqual(res_1, rk.N1())

    def test_n2(self):
        rk = RK1(cdc, libs, libs_cdc)
        self.assertEqual(res_2, rk.N2())


    def test_n3(self):
        rk = RK1(cdc, libs, libs_cdc)
        self.assertEqual(res_3, rk.N3())



if __name__ == '__main__':
    unittest.main()
