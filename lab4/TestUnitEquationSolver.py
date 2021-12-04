import math
import unittest
from lab4.tests.steps.EquationSolver import EquationSolver


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
        self.assertEqual(self.solver.result.sort(), [2].sort())

    def test_result2(self):
        self.solver.ratio = [1, -6, 5]
        self.solver.get_roots()
        self.assertEqual(self.solver.result.sort(), [1, -1, math.sqrt(5), -math.sqrt(5)].sort())

    def test_result3(self):
        self.solver.ratio = [1, 14, 48]
        self.solver.get_roots()
        self.assertEqual(self.solver.result.sort(), None)


if __name__ == "__main__":
    unittest.main()
