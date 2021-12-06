Feature: Test EquationSolver

  Scenario: Run a simple test
    Given the user enters ratio 1, 1, -20
    When Finding roots
    Then Test roots 2, -2
