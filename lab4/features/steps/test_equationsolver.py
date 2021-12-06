from EquationSolver import EquationSolver

from behave import *


@given(u'the user enters ratio {a}, {b}, {c}')
def step_impl(context, a, b, c):
    context.solver = EquationSolver
    context.solver.ratio = list(map(int, [a, b, c]))


@when('Finding roots')
def asd_impl(context):
    context.result = context.solver.get_roots(context.solver)


@then('Test roots {r1}, {r2}')
def abc_impl(context, r1, r2):
    a = sorted(context.result)
    b = sorted(list(map(float, [r1, r2])))

    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                assert a[i] == b[j]
