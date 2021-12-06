import math
import unittest
from EquationSolver import EquationSolver


class TestEquation(unittest.TestCase):
    def setUp(self):
        self.solver = EquationSolver()

    def test_ratio1(self):
        self.solver.ratio = [1, 1, -20]
        self.assertEqual(self.solver.ratio, [1.0, 1.0, -20.0])

    def test_ratio2(self):
        self.solver.ratio = [0, 0, 0]
        self.assertEqual(self.solver.ratio, [0, 0, 0])

    def test_result(self):
        self.solver.ratio = [1, 1, -20]
        self.solver.get_roots()
        self.assertEqual(sorted(self.solver.result), sorted([-2, 2]))

    def test_result2(self):
        self.solver.ratio = [1, -6, 5]
        self.solver.get_roots()
        self.assertEqual(sorted(self.solver.result), sorted([1, -1, math.sqrt(5), -math.sqrt(5)]))

    def test_result3(self):
        self.solver.ratio = [1, 14, 48]
        self.solver.get_roots()
        self.assertEqual(self.solver.result, [])


if __name__ == "__main__":
    unittest.main()
