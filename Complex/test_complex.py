from Complex import Complex
import pytest


def test_equality1():
    c1 = Complex(4, 6)
    c2 = Complex(4, 6)
    assert c1 == c2


def test_equality2():
    c1 = Complex(-5.5, 0)
    c2 = Complex(-5.5, 0)
    assert c1 == c2


def test_inequality():
    c1 = Complex(-5, 0)
    c2 = Complex(-6, 0)
    assert c1 != c2


def test_add():
    c1 = Complex(1, 2)
    c2 = Complex(-5, 10)
    assert c1 + c2 == Complex(-4, 12)


def test_add_zero():
    c1 = Complex(1.1, 2.2)
    c2 = Complex(0, 0)
    assert c1 + c2 == c1


def test_subtract():
    c1 = Complex(1, 2)
    c2 = Complex(-5, 10)
    assert c1 - c2 == Complex(6, -8)


def test_subtract_zero():
    c1 = Complex(1.1, 2.2)
    c2 = Complex(0, 0)
    assert c1 - c2 == c1


def test_mul():
    c1 = Complex(2, 0)
    c2 = Complex(0, -1.5)
    assert c1 * c2 == Complex(0, -3)


def test_mul2():
    c1 = Complex(1, 1)
    c2 = Complex(2, -2)
    assert c1 * c2 == Complex(4, 0)


def test_conjugate():
    c1 = Complex(4, 3)
    assert c1.conjugate() == Complex(4, -3)


def test_div():
    c1 = Complex(0, 4)
    c2 = Complex(1, 0)
    assert c1 / c2 == Complex(0, 4)


def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        c1 = Complex(0, 4)
        c2 = Complex(0, 0)
        c3 = c1/c2


def test_repr():
    c1 = Complex(5, 5)
    assert str(c1) == "5 + (5)i"


def test_repr2():
    c1 = Complex(-5, -5)
    assert str(c1) == "-5 + (-5)i"
