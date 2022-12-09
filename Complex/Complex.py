import math


class Complex:

    def __init__(self, a: float = 0, b: float = 0):
        self.re: float = a
        self.im: float = b

    def __repr__(self):
        return f"{self.re} + ({self.im})i"

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __truediv__(self, other):
        tmp = self * other.conjugate()
        return Complex(tmp.re / float(other) ** 2, tmp.im / float(other) ** 2)

    def conjugate(self):
        return Complex(self.re, -self.im)

    def __float__(self):
        return math.sqrt(self.re ** 2 + self.im ** 2)

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im
