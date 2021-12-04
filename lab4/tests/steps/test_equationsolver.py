import EquationSolver

import pytest
from pytest_bdd import scenario, given, when, then, parsers


@scenario('test.feature', 'Run a simple test')
def test_find():
    pass


@pytest.fixture
def solver():
    a = EquationSolver
    yield a


@given(parsers.parse('the user enters ratio "{coefs}"'))
def collect(solver, coefs):
    solver.ratio = map(float, coefs.split(' ,'))


@when('Finding roots')
def find(solver):
    pass
    solver.get_roots()


@then(parsers.parse('Roots are find for ratio "{answer}"'))
def asd(solver, answer):
    assert solver.result == map(float, answer.split(' ,'))
