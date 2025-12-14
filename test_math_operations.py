import pytest
from math_operations import div, addThree, mulThree, add, sub


@pytest.mark.positive
def test_add_valid():
    # basic integers and zeros
    assert add(0, 0) == 0
    assert add(1, 2) == 3
    assert add(-5, 2) == -3
    # floats
    assert add(1.5, 2.5) == pytest.approx(4.0)
    # large and mixed signs
    assert add(1_000_000_000, -1_000_000_000) == 0
    # commutativity spot-check
    a, b = -7, 3.25
    assert add(a, b) == add(b, a)


@pytest.mark.negative
def test_add_type_errors():
    # invalid operand types
    for x, y in [("1", 2), (None, 3), ({}, 1), ([], 0)]:
        with pytest.raises(TypeError):
            add(x, y)
    # wrong argument count
    with pytest.raises(TypeError):
        add(1)  # missing one arg
    with pytest.raises(TypeError):
        add(1, 2, 3)  # too many args


@pytest.mark.positive
def test_sub_valid():
    # basic integers and zeros
    assert sub(0, 0) == 0
    assert sub(5, 2) == 3
    assert sub(-5, -2) == -3
    # floats
    assert sub(5.5, 2.25) == pytest.approx(3.25)
    # non-commutativity check
    a, b = 9, 4
    assert sub(a, b) != sub(b, a)


@pytest.mark.negative
def test_sub_type_errors():
    # invalid operand types
    for x, y in [("1", 2), (None, 3), ({}, 1), ((), 0)]:
        with pytest.raises(TypeError):
            sub(x, y)
    # wrong argument count
    with pytest.raises(TypeError):
        sub(1)
    with pytest.raises(TypeError):
        sub(1, 2, 3)


@pytest.mark.positive
def test_addThree_valid():
    # zeros identity
    assert addThree(0, 0, 0) == 0
    # basic integers
    assert addThree(1, 2, 3) == 6
    assert addThree(-1, -2, -3) == -6
    # floats
    assert addThree(1.5, 2.5, 3.0) == pytest.approx(7.0)
    # mixed signs and order-insensitive sum
    a, b, c = -10, 4.5, 3
    total = addThree(a, b, c)
    assert total == pytest.approx(a + b + c)


@pytest.mark.negative
def test_addThree_type_errors_and_arity():
    # invalid operand types
    for args in [
        ("1", 2, 3),
        (None, 2, 3),
        ({}, 2, 3),
        ([], 2, 3),
    ]:
        with pytest.raises(TypeError):
            addThree(*args)
    # wrong argument count
    with pytest.raises(TypeError):
        addThree(1, 2)  # too few
    with pytest.raises(TypeError):
        addThree(1, 2, 3, 4)  # too many


@pytest.mark.positive
def test_mulThree_valid():
    # basic integers
    assert mulThree(1, 2, 3) == 6
    assert mulThree(-1, 2, 3) == -6
    # floats
    assert mulThree(1.5, 2.0, 2.0) == pytest.approx(6.0)
    # identity with one
    assert mulThree(1, 7, 5) == 35
    # zero short-circuit
    assert mulThree(0, 999, -123) == 0


@pytest.mark.negative
def test_mulThree_type_errors_and_arity():
    # invalid operand types
    for args in [
        ("1", 2.5, 3),  # string * float -> TypeError
        (None, 2, 3),
        ({}, 2, 3),
        ([], 2.5, 3),  # list * float -> TypeError
    ]:
        with pytest.raises(TypeError):
            mulThree(*args)
    # wrong argument count
    with pytest.raises(TypeError):
        mulThree(1, 2)  # too few
    with pytest.raises(TypeError):
        mulThree(1, 2, 3, 4)  # too many


@pytest.mark.positive
def test_div_valid():
    # integers
    assert div(6, 3) == 2
    assert div(-6, 3) == -2
    # floats
    assert div(5, 2) == pytest.approx(2.5)
    # zero numerator
    assert div(0, 5) == 0


@pytest.mark.negative
def test_div_zero_division():
    for a in [0, 5, -3.2]:
        with pytest.raises(ZeroDivisionError):
            div(a, 0)


@pytest.mark.negative
def test_div_type_errors_and_arity():
    # invalid operand types
    for x, y in [("1", 2), (None, 3), ({}, 1), ([], 1)]:
        with pytest.raises(TypeError):
            div(x, y)
    # wrong argument count
    with pytest.raises(TypeError):
        div(1)  # too few
    with pytest.raises(TypeError):
        div(1, 2, 3)  # too many