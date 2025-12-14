import pytest
from math_operations import add, addThree, mulThree, div


# add tests
@pytest.mark.positive
def test_add_integers_positive():
    assert add(2, 3) == 5


@pytest.mark.positive
def test_add_mixed_float_positive():
    assert add(2.5, 0.5) == 3.0


@pytest.mark.positive
def test_add_strings_positive():
    assert add("foo", "bar") == "foobar"


@pytest.mark.negative
def test_add_type_error_negative():
    with pytest.raises(TypeError):
        add("1", 2)


@pytest.mark.negative
def test_add_too_many_args_negative():
    with pytest.raises(TypeError):
        # Too many positional arguments should raise TypeError
        add(1, 2, 3)  # type: ignore[misc]


@pytest.mark.negative
def test_add_with_none_negative():
    with pytest.raises(TypeError):
        add(None, 1)  # type: ignore[arg-type]


# addThree tests
@pytest.mark.positive
def test_addThree_integers_positive():
    assert addThree(1, 2, 3) == 6


@pytest.mark.positive
def test_addThree_floats_positive():
    assert addThree(1.1, 2.2, 3.3) == pytest.approx(6.6)


@pytest.mark.positive
def test_addThree_strings_positive():
    assert addThree("a", "b", "c") == "abc"


@pytest.mark.negative
def test_addThree_missing_arg_negative():
    with pytest.raises(TypeError):
        addThree(1, 2)  # type: ignore[misc]


@pytest.mark.negative
def test_addThree_invalid_type_mix_negative():
    with pytest.raises(TypeError):
        addThree("a", 1, "b")


# mulThree tests
@pytest.mark.positive
def test_mulThree_integers_positive():
    assert mulThree(2, 3, 4) == 24


@pytest.mark.positive
def test_mulThree_float_mix_positive():
    assert mulThree(2.0, 3, 0.5) == pytest.approx(3.0)


@pytest.mark.positive
def test_mulThree_string_repetition_positive():
    assert mulThree("ab", 2, 3) == "ab" * 6


@pytest.mark.positive
def test_mulThree_zero_positive():
    assert mulThree(10, 0, 5) == 0


@pytest.mark.negative
def test_mulThree_invalid_string_float_negative():
    with pytest.raises(TypeError):
        mulThree("a", 2.5, 2)


@pytest.mark.negative
def test_mulThree_missing_arg_negative():
    with pytest.raises(TypeError):
        mulThree(1, 2)  # type: ignore[misc]


# div tests
@pytest.mark.positive
def test_div_integers_positive():
    assert div(6, 3) == 2.0


@pytest.mark.positive
def test_div_non_divisible_positive():
    assert div(3, 2) == 1.5


@pytest.mark.positive
def test_div_negative_values_positive():
    assert div(-8, 2) == -4.0


@pytest.mark.positive
def test_div_bool_divisor_true_positive():
    assert div(10, True) == 10.0


@pytest.mark.negative
def test_div_by_zero_negative():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


@pytest.mark.negative
def test_div_by_false_negative():
    with pytest.raises(ZeroDivisionError):
        div(5, False)


@pytest.mark.negative
def test_div_invalid_type_negative():
    with pytest.raises(TypeError):
        div("10", 2)