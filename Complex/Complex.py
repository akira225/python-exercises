import math


class Complex:

    def __init__(self, a=0, b=0):
        self.re = a
        self.im = b

    def __repr__(self):
        return f"{self.re} + ({self.im})i"

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re*other.re - self.im*other.im, self.re*other.im + self.im*other.re)

    def __rdiv__(self, other):
        return self*other.conjugate/float(other)**2

    def conjugate(self):
        return Complex(self.re, -self.im)

    def __float__(self):
        return math.sqrt(self.re**2 + self.im**2)

