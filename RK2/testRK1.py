import unittest

from RK1 import RK1
from ds import cdc, libs, libs_cdc



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
