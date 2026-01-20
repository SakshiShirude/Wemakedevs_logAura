import pytest
from math_operations import add, addThree, mulThree, div, exp


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-5, 5, 0),
        (1.5, 2.5, pytest.approx(4.0)),
        (10**6, 10**6, 2 * 10**6),
    ],
)
def test_add_valid(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "a,b",
    [
        (1, "2"),
        ("1", 2),
        ([1], 2),
        (None, 1),
    ],
)
def test_add_invalid_type_mismatch(a, b):
    with pytest.raises(TypeError):
        add(a, b)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (-1, -2, -3, -6),
        (1.1, 2.2, 3.3, pytest.approx(6.6)),
        ("a", "b", "c", "abc"),
    ],
)
def test_addThree_valid(a, b, c, expected):
    assert addThree(a, b, c) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "a,b,c",
    [
        ("1", 2, 3),
        (1, "2", 3),
        (1, 2, "3"),
        (None, 2, 3),
    ],
)
def test_addThree_invalid_mixed_types(a, b, c):
    with pytest.raises(TypeError):
        addThree(a, b, c)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (-1, 2, -3, 6),
        (0, 5, 7, 0),
        (2.5, 2, 3, pytest.approx(15.0)),
        ("ab", 2, 3, "abababababab"),  # string replication: ("ab"*2)*3
    ],
)
def test_mulThree_valid(a, b, c, expected):
    assert mulThree(a, b, c) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "a,b,c",
    [
        ("a", "b", 3),  # cannot multiply sequence by non-int of type 'str'
        ("a", 2.5, 2),   # float multiplier invalid for sequence
        ({}, 2, 3),       # dict not multiplicable
    ],
)
def test_mulThree_invalid_types(a, b, c):
    with pytest.raises(TypeError):
        mulThree(a, b, c)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2),
        (-9, 3, -3),
        (1, 4, 0.25),
        (1, 3, pytest.approx(1/3)),
        (2.5, 0.5, pytest.approx(5.0)),
    ],
)
def test_div_valid(a, b, expected):
    result = div(a, b)
    if isinstance(expected, float) and expected != int(expected):
        assert result == pytest.approx(expected)
    else:
        assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize("a,b", [(1, 0), (1, 0.0), (-5, 0)])
def test_div_by_zero(a, b):
    with pytest.raises(ZeroDivisionError):
        div(a, b)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 8),
        (5, 0, 1),
        (-2, 3, -8),
        (2, -3, pytest.approx(0.125)),
        (9, 0.5, 3.0),
    ],
)
def test_exp_valid(a, b, expected):
    result = exp(a, b)
    if isinstance(expected, float) and expected != int(expected):
        assert result == pytest.approx(expected)
    else:
        assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize("a,b", [(0, -1), (0.0, -2)])
def test_exp_zero_to_negative_power_raises(a, b):
    with pytest.raises(ZeroDivisionError):
        exp(a, b)


@pytest.mark.negative
@pytest.mark.parametrize("a,b", [("2", 3), (2, "3"), (None, 2)])
def test_exp_invalid_types(a, b):
    with pytest.raises(TypeError):
        exp(a, b)