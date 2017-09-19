#
# File:   designLab01Work.py
# Author: 6.01 Staff
# Date:   02-Sep-11
#
# Below are templates for your answers to three parts of Design Lab 1

#-----------------------------------------------------------------------------

def fib(n):
    # Delete the pass statement below and insert your own code
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#-----------------------------------------------------------------------------

class V2:
    # Delete the pass statement below and insert your own code
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def add(self, b):
        x = self.getX() + b.getX()
        y = self.getY() + b.getY()
        return V2(x, y)

    def mul(self, b):
        y = self.getX()*b
        x = self.getY()*b
        return V2(x, y)

    def __add__(self, v):
        return self.add(v)

    def __mul__(self, c):
        return self.mul(c)

    def __str__(self):
        return 'V2[' + str(self.x) + ', ' + str(self.y) + ']'
        
    
#-----------------------------------------------------------------------------

class Polynomial:
    # Delete the pass statement below and insert your own code
    def __init__(self, coefficients):
        float_list = []
        for coff in coefficients:
            float_list.append(float(coff))
        self.coeffs = float_list

    def coeff(self, i):
        return self.coeffs[i]

    def add(self, other):
        len_diff = abs(len(other.coeffs) - len(self.coeffs))
        if len(other.coeffs) >= len(self.coeffs):
            new_pol = self.coeffs
            new_pol = [0] * len_diff + new_pol
            for i in range(len(new_pol)):
                new_pol[i] = other.coeff(i) + new_pol[i]
        else:
            new_pol = other.coeffs
            new_pol = [0] * len_diff + new_pol
            for i in range(len(new_pol)):
                new_pol[i] = self.coeff(i) + new_pol[i]
        return Polynomial(new_pol)

    def mul(self, other):
        result = [0]*(len(self.coeffs) + len(other.coeffs) - 1)
        for id1, i in enumerate(self.coeffs):
            for id2, j in enumerate(other.coeffs):
                result[id1+id2] += i*j
        return Polynomial(result)

    def val(self, v):
        result = 0
        reve = self.coeffs[::-1]
        for i in range(len(reve)):
            result += reve[i]*v**i
        return result

    def roots(self):
        root = []
        if len(self.coeffs) == 2:
            root = -self.coeff(1)/self.coeff(0)
        elif len(self.coeffs) == 3:
            root.append((-self.coeff(1) + (self.coeff(1)**2 - 4*self.coeff(0)*self.coeff(2))**0.5)/(2*self.coeff(0)))
            root.append((-self.coeff(1) - (self.coeff(1)**2 - 4*self.coeff(0)*self.coeff(2))**0.5)/(2*self.coeff(0)))
        return root

    def __str__(self):
        po_string = ''
        l = len(self.coeffs) - 1
        for i in range(l + 1):
            if l-i >= 2:
                po_string += str(self.coeff(i)) + ' z**' + str(l - i) + ' + '
            elif l-i == 1:
                po_string += str(self.coeff(i)) + ' z' + ' + '
            elif l-i == 0:
                po_string += str(self.coeff(i))
        return po_string

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

    def __call__(self, x):
        return self.val(x)

    def __repr__(self):
        return str(self)