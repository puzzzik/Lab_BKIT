# -*- coding: utf-8 -*-

import sys
import math


class EquationSolver:
    def __init__(self):
        self.result = []
        self.coefs = [0, 0, 0]

    def get_coefs(self, a, b, c):
        self.coefs = [a, b, c]

    def input_coefs(self):
        self._addcoef(0, 'Введите коэффициент А:')
        while self.coefs[0] == 0:
            self._addcoef(0, 'Введите коэффициент А:')
        self._addcoef(1, 'Введите коэффициент B:')
        self._addcoef(2, 'Введите коэффициент C:')

    def _addcoef(self, index, prompt):
        try:
            coef_str = sys.argv[index + 1]
            if sys.argv[1] == '0':
                int('bn')
            float(coef_str)
        except:
            flag = True
            while flag:
                print(prompt)
                coef_str = str(input())
                if coef_str.isdigit() or (coef_str[0] == '-' and coef_str[1:].isdigit()):
                    flag = False

        self.coefs[index] = float(coef_str)

    def get_roots(self):
        result = set()
        a, b, c = self.coefs
        D = b * b - 4 * a * c
        if D == 0.0:
            root = -b / (2.0 * a)
            if root > 0:
                result.add(math.sqrt(root))
                result.add(-math.sqrt(root))
            elif root == 0:
                result.add(abs(math.sqrt(root)))

        elif D > 0.0:
            root1, root2, root3, root4 = None, None, None, None
            sqD = math.sqrt(D)
            rootSq1 = (-b + sqD) / (2.0 * a)
            rootSq2 = (-b - sqD) / (2.0 * a)

            if rootSq1 > 0:
                root1 = math.sqrt(rootSq1)
                root2 = -math.sqrt(rootSq1)
            elif rootSq1 == 0:
                root1 = abs(math.sqrt(rootSq1))

            if rootSq2 > 0:
                root3 = math.sqrt(rootSq2)
                root4 = -math.sqrt(rootSq2)
            elif rootSq2 == 0:
                root3 = abs(math.sqrt(rootSq2))
            result.add(root1)
            result.add(root2)
            result.add(root3)
            result.add(root4)

            self.result = list(filter(lambda x: x is not None, result))

    def printResult(self):
        if len(self.result) == 0:
            print("Нет корней")
        elif len(self.result) == 1:
            print("Один корень: {}".format(self.result[0]))
        elif len(self.result) == 2:
            print("Два корня: {} и {}".format(self.result[0], self.result[1]))
        elif len(self.result) == 3:
            print("Три корня: {}, {} и {}".format(self.result[0], self.result[1], self.result[2]))
        else:
            print("Четыре корня: {}, {}, {} и {}". format(self.result[0], self.result[1], self.result[2], self.result[3]))


def main():
    solver = EquationSolver()
    solver.input_coefs()
    solver.get_roots()
    solver.printResult()


if __name__ == "__main__":
    main()
