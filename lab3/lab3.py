# Тесты TDD

from lab1Module import findTrueRoots, solve_biquadratic
import math

def test_solve_biquadratic_real_roots():
    # Test case with real roots
    roots = solve_biquadratic(1, -3, 2)

    expected_roots = [math.sqrt(2), -math.sqrt(2), 1.0, -1.0]  # roots are (1, 2) and their negatives
    assert findTrueRoots(roots) == expected_roots

def test_solve_biquadratic_complex_roots():
    # Test case with complex roots
    roots = solve_biquadratic(1, 1, 1)
    expected_roots = ()  # no real roots
    assert roots == expected_roots

def test_find_true_roots():
    # Test case for find_true_roots function
    roots = [1 + 0j, 2 + 0j, 0 + 1j, -1 - 1j]  # mix of real and complex roots
    true_roots = findTrueRoots(roots)
    expected_true_roots = [1, 2]
    assert true_roots == expected_true_roots