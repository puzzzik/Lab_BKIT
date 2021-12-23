# -*- coding: utf-8 -*-

import abc


class Figure(abc.ABC):
    """
    Абстрактный класс «Геометрическая фигура»
    """

    @abc.abstractmethod
    def square(self):
        """
        содержит виртуальный метод для вычисления площади фигуры.
        """
        pass
