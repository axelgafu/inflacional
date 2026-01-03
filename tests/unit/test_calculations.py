import pytest
from banxico_report.api.exchange import calculate_fix_variation

def test_calculate_fix_variation_simple():
    # FIX(t) = 17.50, FIX(t-1) = 17.40
    # Variation should be 0.10
    variation = calculate_fix_variation(17.50, 17.40)
    assert variation == 0.1000

def test_calculate_fix_variation_negative():
    # FIX(t) = 17.40, FIX(t-1) = 17.50
    # Variation should be -0.10
    variation = calculate_fix_variation(17.40, 17.50)
    assert variation == -0.1000

def test_calculate_fix_variation_precision():
    # Testing 4 decimal precision
    variation = calculate_fix_variation(17.50555, 17.40444)
    # 17.50555 - 17.40444 = 0.10111 -> 0.1011
    assert variation == 0.1011
