import pytest
from math_operations import div, addThree, mulThree


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5.0),
        (3, 2, 1.5),
        (-6, 3, -2.0),
        (7.5, 2.5, 3.0),
        (-9, -3, 3.0),
    ],
)
def test_div_valid(a, b, expected):
    assert div(a, b) == pytest.approx(expected)


@pytest.mark.negative
@pytest.mark.parametrize("a", [0, 1, -1, 3.5])
def test_div_by_zero(a):
    with pytest.raises(ZeroDivisionError):
        div(a, 0)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (1.5, 2.5, 3.0, 7.0),
        ("a", "b", "c", "abc"),
        (0, 0, 0, 0),
    ],
)
def test_addThree_valid(a, b, c, expected):
    res = addThree(a, b, c)
    if isinstance(expected, float):
        assert res == pytest.approx(expected)
    else:
        assert res == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "a,b,c",
    [
        ("a", 1, 2),
        (1, "2", 3),
        (None, 1, 2),
    ],
)
def test_addThree_type_error(a, b, c):
    with pytest.raises(TypeError):
        addThree(a, b, c)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (2, 3, 4, 24),
        (-1, 2, -3, 6),
        (5, 0, 7, 0),
        (1.5, 2, 3, 9.0),
        ("a", 2, 3, "aaaaaa"),
    ],
)
def test_mulThree_valid(a, b, c, expected):
    res = mulThree(a, b, c)
    if isinstance(expected, float):
        assert res == pytest.approx(expected)
    else:
        assert res == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "a,b,c",
    [
        (None, 2, 3),
        (2, "b", "c"),
        ([1], [2], 3),
    ],
)
def test_mulThree_type_error(a, b, c):
    with pytest.raises(TypeError):
        mulThree(a, b, c)