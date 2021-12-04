Feature: Test EquationSolver

  Scenario: Run a simple test
    Given the user enters ratio "1, 1, -20"
    When Finding roots
    Then Roots are find for ratio "2"
