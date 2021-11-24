import math
import unittest
from EquationSolver import EquationSolver


class TestEquation(unittest.TestCase):
    def setUp(self):
        self.solver = EquationSolver()

    def test_coefs1(self):
        self.solver.get_coefs(1, 1, -20)
        self.assertEqual(self.solver.coefs, [1.0, 1.0, -20.0])

    def test_coefs2(self):
        self.solver.get_coefs(0, 0, 0)
        self.assertEqual(self.solver.coefs, [0, 0, 0])

    def test_result(self):
        self.solver.get_coefs(1, 1, -20)
        self.solver.get_roots()
        self.assertEqual(self.solver.result.sort(), [2].sort())

    def test_result2(self):
        self.solver.get_coefs(1, -6, 5)
        self.solver.get_roots()
        self.assertEqual(self.solver.result.sort(), [1, -1, math.sqrt(5), -math.sqrt(5)].sort())

    def test_result3(self):
        self.solver.get_coefs(1, 14, 48)
        self.solver.get_roots()
        self.assertEqual(self.solver.result.sort(), None)


if __name__ == "__main__":
    unittest.main()
