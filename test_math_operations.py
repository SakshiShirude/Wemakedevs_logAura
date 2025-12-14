import pytest
from math_operations import div, addThree, mulThree, add, exp


# add
@pytest.mark.positive
def test_add_integers():
    assert add(2, 3) == 5


@pytest.mark.positive
def test_add_floats():
    assert add(2.5, 0.5) == pytest.approx(3.0)


@pytest.mark.positive
def test_add_zero_and_negative():
    assert add(0, -5) == -5
    assert add(-2, 2) == 0


@pytest.mark.negative
def test_add_type_error_str_int():
    with pytest.raises(TypeError):
        add("a", 1)


@pytest.mark.negative
def test_add_type_error_none():
    with pytest.raises(TypeError):
        add(None, 1)


@pytest.mark.negative
def test_add_type_error_list():
    with pytest.raises(TypeError):
        add([1], 2)


# addThree
@pytest.mark.positive
def test_addThree_integers():
    assert addThree(1, 2, 3) == 6


@pytest.mark.positive
def test_addThree_mixed_floats():
    assert addThree(1.5, 2, 0.5) == pytest.approx(4.0)


@pytest.mark.positive
def test_addThree_with_zero_and_negatives():
    assert addThree(-1, 0, 1) == 0


@pytest.mark.negative
def test_addThree_type_error_str():
    with pytest.raises(TypeError):
        addThree("x", 1, 2)


@pytest.mark.negative
def test_addThree_type_error_none():
    with pytest.raises(TypeError):
        addThree(1, None, 3)


# mulThree
@pytest.mark.positive
def test_mulThree_integers():
    assert mulThree(2, 3, 4) == 24


@pytest.mark.positive
def test_mulThree_includes_zero():
    assert mulThree(5, 0, 10) == 0


@pytest.mark.positive
def test_mulThree_sign_and_float():
    assert mulThree(-2, 0.5, 3) == pytest.approx(-3.0)


@pytest.mark.negative
def test_mulThree_type_error_str_str_int():
    with pytest.raises(TypeError):
        mulThree("a", "b", 2)


@pytest.mark.negative
def test_mulThree_type_error_float_str():
    with pytest.raises(TypeError):
        mulThree(1.5, "a", 2)


# div
@pytest.mark.positive
def test_div_integers():
    assert div(4, 2) == pytest.approx(2.0)


@pytest.mark.positive
def test_div_floats():
    assert div(5.0, 2.0) == pytest.approx(2.5)


@pytest.mark.positive
def test_div_negative_values():
    assert div(-9, 3) == pytest.approx(-3.0)


@pytest.mark.negative
def test_div_zero_division_int():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


@pytest.mark.negative
def test_div_zero_division_float():
    with pytest.raises(ZeroDivisionError):
        div(1.0, 0.0)


@pytest.mark.negative
def test_div_type_error_string_numerator():
    with pytest.raises(TypeError):
        div("10", 2)


@pytest.mark.negative
def test_div_type_error_string_denominator():
    with pytest.raises(TypeError):
        div(10, "2")


# exp
@pytest.mark.positive
def test_exp_positive_integer():
    assert exp(2, 3) == 8


@pytest.mark.positive
def test_exp_zero_exponent():
    assert exp(5, 0) == 1


@pytest.mark.positive
def test_exp_zero_base_zero_exponent():
    assert exp(0, 0) == 1


@pytest.mark.positive
def test_exp_negative_exponent():
    assert exp(2, -3) == pytest.approx(0.125)


@pytest.mark.positive
def test_exp_negative_base_integer_exponent():
    assert exp(-2, 3) == -8
    assert exp(-2, 4) == 16


@pytest.mark.positive
def test_exp_float_exponent_square_root():
    assert exp(9, 0.5) == pytest.approx(3.0)


@pytest.mark.negative
def test_exp_type_error_base_str():
    with pytest.raises(TypeError):
        exp("2", 3)


@pytest.mark.negative
def test_exp_type_error_exponent_str():
    with pytest.raises(TypeError):
        exp(2, "3")


@pytest.mark.negative
def test_exp_zero_to_negative_exponent_zerodivision():
    with pytest.raises(ZeroDivisionError):
        exp(0, -1)