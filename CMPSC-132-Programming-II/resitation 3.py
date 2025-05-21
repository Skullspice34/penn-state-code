class Complex:
    """ Complex number of the form a + bi, where a and b are real numbers, and i is an indeterminate satisfying i2 = −1 """

    def __init__(self,r,i):
        self._real = r
        self._imag = i
    def __str__(self):
        """Display complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"
        else:
           return f"{self._real} - {abs(self._imag)}i"

    __repr__ = __str__

    def conjugate(self):
        """Returns a Complex object that represents the complex conjugate"""
        opposite = self._imag * - 1
        return Complex(self._real,opposite)


    def __mul__(self,other):
        """Multiply two Complex numbers"""
        ans = None
        if isinstance(other, Complex):
            real = (self._real * other._real - self._imag * other._imag)
            imaginary = (self._real * other._imag + self._imag * other._real)
            ans = Complex(real, imaginary)
        else:
            real = (self._real * other)
            imaginary = (self._imag* other)
            ans = Complex(real, imaginary)
        return ans

    def __rmul__(self,other):
        return self * other


a = Complex(5,-6)
b = Complex(2,14)
print (a * b)
print (b * 5)
print (5 * b)
print (isinstance(5 * b, Complex))
print (a.conjugate())
print (b.conjugate())
