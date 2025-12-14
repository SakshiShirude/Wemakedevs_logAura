import pytest
from math_operations import div, addThree, mulThree, add


# -------------------- add --------------------
@pytest.mark.positive
def test_add_integers():
    assert add(2, 3) == 5


@pytest.mark.positive
def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3, rel=1e-12, abs=1e-12)


@pytest.mark.positive
def test_add_negatives():
    assert add(-1, -5) == -6


@pytest.mark.positive
def test_add_booleans_behave_as_ints():
    # True == 1, False == 0
    assert add(True, 2) == 3


@pytest.mark.positive
def test_add_strings_concatenation():
    assert add("foo", "bar") == "foobar"


@pytest.mark.positive
def test_add_lists_concatenation():
    assert add([1, 2], [3]) == [1, 2, 3]


@pytest.mark.negative
def test_add_type_mismatch_int_and_str_raises():
    with pytest.raises(TypeError):
        add(1, "2")


@pytest.mark.negative
def test_add_type_mismatch_str_and_int_raises():
    with pytest.raises(TypeError):
        add("2", 1)


# -------------------- addThree --------------------
@pytest.mark.positive
def test_addThree_all_integers():
    assert addThree(1, 2, 3) == 6


@pytest.mark.positive
def test_addThree_mixed_numeric_types():
    assert addThree(1, 2.5, -3) == 0.5


@pytest.mark.positive
def test_addThree_string_concatenation():
    assert addThree("a", "b", "c") == "abc"


@pytest.mark.negative
def test_addThree_type_mismatch_raises():
    with pytest.raises(TypeError):
        addThree("a", 1, "b")


# -------------------- mulThree --------------------
@pytest.mark.positive
def test_mulThree_integers():
    assert mulThree(2, 3, 4) == 24


@pytest.mark.positive
def test_mulThree_with_zero_short_circuits_to_zero():
    assert mulThree(0, 99, 1000) == 0


@pytest.mark.positive
def test_mulThree_with_negatives():
    assert mulThree(-2, 3, 4) == -24


@pytest.mark.positive
def test_mulThree_string_replication():
    assert mulThree("a", 2, 3) == "a" * 2 * 3 == "aaaaaa"


@pytest.mark.negative
def test_mulThree_invalid_string_times_string_then_int():
    with pytest.raises(TypeError):
        mulThree("a", "b", 2)


@pytest.mark.negative
def test_mulThree_invalid_string_times_float_after_valid_int():
    with pytest.raises(TypeError):
        mulThree("a", 2, 2.5)


# -------------------- div --------------------
@pytest.mark.positive
def test_div_integers_exact_result_float():
    assert div(4, 2) == 2.0


@pytest.mark.positive
def test_div_float_result():
    assert div(1, 2) == pytest.approx(0.5)


@pytest.mark.positive
def test_div_with_negatives():
    assert div(-6, 3) == -2.0


@pytest.mark.negative
def test_div_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


@pytest.mark.negative
def test_div_non_numeric_numerator_raises():
    with pytest.raises(TypeError):
        div("a", 1)


@pytest.mark.negative
def test_div_non_numeric_denominator_raises():
    with pytest.raises(TypeError):
        div(1, "0")