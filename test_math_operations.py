import pytest
from math_operations import div, add, addThree, mulThree, mul3


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2),
        (7, 2, 3.5),
        (-8, 2, -4),
        (0, 5, 0),
        (5, -2, -2.5),
        (5.5, 2, 2.75),
        (-9.0, -3, 3.0),
    ],
)
def test_div_basic(a, b, expected):
    result = div(a, b)
    # Use approx for floating point comparisons
    assert result == pytest.approx(expected)


@pytest.mark.negative
@pytest.mark.parametrize("a,b", [(1, 0), (0, 0), (-5, 0), (1.0, 0.0)])
def test_div_by_zero(a, b):
    with pytest.raises(ZeroDivisionError):
        div(a, b)


@pytest.mark.negative
@pytest.mark.parametrize(
    "a,b",
    [
        ("10", 2),
        (10, "2"),
        (None, 1),
        (1, None),
        ([1, 2], 1),
        (1, [1, 2]),
        ({"a": 1}, 2),
    ],
)
def test_div_invalid_types(a, b):
    with pytest.raises(TypeError):
        div(a, b)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 2, 1),
        (1.5, 2.5, 4.0),
        (0, 0, 0),
        (10**10, 10**10, 2 * 10**10),
        (-3.2, -2.8, -6.0),
    ],
)
def test_add_valid(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.negative
@pytest.mark.parametrize(
    "a,b",
    [
        (1, "2"),
        ("a", 1),
        (None, 3),
        ([], {}),
        ({}, []),
    ],
)
def test_add_invalid_types(a, b):
    with pytest.raises(TypeError):
        add(a, b)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (-1, 2, 3, 4),
        (1.5, 2.5, 3.0, 7.0),
        (0, 0, 0, 0),
        (10**6, 10**6, 10**6, 3 * 10**6),
        (-3.2, -2.8, 1.0, -5.0),
    ],
)
def test_addThree_valid(a, b, c, expected):
    assert addThree(a, b, c) == pytest.approx(expected)


@pytest.mark.negative
@pytest.mark.parametrize(
    "a,b,c",
    [
        (1, 2, "3"),
        ("1", 2, 3),
        (None, 0, 0),
        ([], 1, 2),
        (1, {}, 3),
    ],
)
def test_addThree_invalid_types(a, b, c):
    with pytest.raises(TypeError):
        addThree(a, b, c)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (2, -3, 4, -24),
        (0, 5, 7, 0),
        (1.5, 2, 2, 6.0),
        (-1, -2, -3, -6),
        (10**3, 10**2, 10, 10**6),
    ],
)
def test_mulThree_valid(a, b, c, expected):
    assert mulThree(a, b, c) == pytest.approx(expected)


@pytest.mark.negative
@pytest.mark.parametrize(
    "a,b,c",
    [
        (2.5, "x", 2),
        ("a", "b", 2),
        (None, 0, 1),
        ([], 1.5, 2),
        (1, {}, 3),
    ],
)
def test_mulThree_invalid_types(a, b, c):
    with pytest.raises(TypeError):
        mulThree(a, b, c)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (2, -3, 4, -24),
        (0, 5, 7, 0),
        (1.5, 2, 2, 6.0),
        (-1, -2, -3, -6),
        (10**3, 10**2, 10, 10**6),
    ],
)
def test_mul3_valid(a, b, c, expected):
    assert mul3(a, b, c) == pytest.approx(expected)


@pytest.mark.negative
@pytest.mark.parametrize(
    "a,b,c",
    [
        (2.5, "x", 2),
        ("a", "b", 2),
        (None, 0, 1),
        ([], 1.5, 2),
        (1, {}, 3),
    ],
)
def test_mul3_invalid_types(a, b, c):
    with pytest.raises(TypeError):
        mul3(a, b, c)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,c",
    [
        (3, 4, 5),
        (1.2, -3, 4),
        (0, 10, -7),
    ],
)
def test_mul3_equals_mulThree(a, b, c):
    assert mul3(a, b, c) == mulThree(a, b, c)