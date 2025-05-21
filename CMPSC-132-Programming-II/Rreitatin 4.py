class Complex:

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

    

class Real(Complex):

    def __init__(self, value):
        super().__init__(value, 0)

    def __mul__(self,other):
        ans = None
        if isinstance(other, Real):
            real = (self._real * other._real - self._imag * other._imag)
            ans = Real(real)
        elif isinstance(other, Complex):
            real = (self._real * other._real - self._imag * other._imag)
            imaginary = (self._real * other._imag + self._imag * other._real)
            ans = Complex(real, imaginary)
        else:
            real = (self._real * other)
            ans = Real(real)
        return ans
    
    def __eq__(self, other):
        if isinstance(other, Real):
         return self._real == other._real
        elif isinstance(other, Complex):
            if other._imag == 0:
                return self._real == other._real
            else:
                return False
        else:
                return False

    def __int__(self):
        return int(self._real)
    
    def __float__(self):
        return float(self._real)


