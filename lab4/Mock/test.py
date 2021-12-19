from unittest import TestCase
from unittest.mock import patch, Mock
import time
from math import sqrt
from main import EquationSolver


class TestSolver(TestCase):
    @patch('main.EquationSolver.input_ratio', return_value=0)
    def test_solver(self, input_ratio):
        solver = EquationSolver
        solver.ratio = [1, 1, -20]
        print(solver.ratio)
        solver.input_ratio()

        solver.get_roots(self=solver)

        a = solver.getResult(self=solver)
        self.assertEqual(sorted(solver.getResult(self=solver)), [-2, 2])


if __name__ == '__main__':
    TestSolver.test_solver()
