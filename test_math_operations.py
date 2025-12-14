import pytest
from math_operations import div, addThree, mulThree, mul


# Positive tests
@pytest.mark.positive
def test_div_integers_positive():
    assert div(10, 2) == 5.0


@pytest.mark.positive
def test_div_negative_division_positive():
    assert div(-10, 2) == -5.0


@pytest.mark.positive
def test_div_floats_positive():
    assert div(7.5, 2.5) == 3.0


@pytest.mark.positive
def test_addThree_integers_positive():
    assert addThree(1, 2, 3) == 6


@pytest.mark.positive
def test_addThree_floats_positive():
    assert addThree(1.5, 2.5, 3.0) == 7.0


@pytest.mark.positive
def test_mulThree_integers_positive():
    assert mulThree(2, 3, 4) == 24


@pytest.mark.positive
def test_mulThree_mixed_positive():
    assert mulThree(-2, 0.5, 3) == -3.0


@pytest.mark.positive
def test_mul_integers_positive():
    assert mul(7, 6) == 42


@pytest.mark.positive
def test_mul_float_positive():
    assert mul(2.5, 4) == 10.0


# Negative tests
@pytest.mark.negative
def test_div_by_zero_negative_int():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


@pytest.mark.negative
def test_div_by_zero_negative_float():
    with pytest.raises(ZeroDivisionError):
        div(1.0, 0.0)


@pytest.mark.negative
def test_div_type_error_negative():
    with pytest.raises(TypeError):
        div("10", 2)


@pytest.mark.negative
def test_addThree_type_error_negative():
    with pytest.raises(TypeError):
        addThree(1, "2", 3)


@pytest.mark.negative
def test_mulThree_type_error_negative():
    with pytest.raises(TypeError):
        mulThree("a", "b", 3)


@pytest.mark.negative
def test_mul_type_error_negative():
    with pytest.raises(TypeError):
        mul("a", "b")