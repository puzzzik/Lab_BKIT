# -*- coding: utf-8 -*-

import unittest
from weather import Weather


class TestBot(unittest.TestCase):
    def test_1(self):
        w = Weather()
        w.city = 'Тула'
        w.country = 'Россия'
        self.assertEqual(w.get_weather().split('\n')[0], 'Tula RU')

    def test_2(self):
        w = Weather()
        w.city = 'asdklfjh'
        w.country = 'hkjagsdf'
        self.assertEqual(w.get_weather(), None)

    def test_3(self):
        w = Weather()
        w.city = 'Стамбул'
        w.country = 'Турция'
        self.assertEqual(w.get_weather().split('\n')[0], 'İstanbul TR')


if __name__ == '__main__':
    unittest.main()
