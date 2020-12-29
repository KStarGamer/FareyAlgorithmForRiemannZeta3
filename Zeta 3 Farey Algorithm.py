from math import *
from mpmath import *
import mpmath
from random import *
from decimal import *
from sympy import *
from fractions import Fraction as Fr

mp.pretty = False
mp.prec = 848
mp.dps = 480

gAttempts = []

def farey(x, N):
    a, b = 0, 1
    c, d = 1, 1
    while (b <= N and d <= N):
        mediant = fdiv(fadd(a, c), fadd(b, d))
        if x == mediant:
            if fadd(b, d) <= N:
                return fadd(a, c), fadd(b, d)
            elif d > b:
                return c, d
            else:
                return a, b
        elif x > mediant:
            a, b = fadd(a, c), fadd(b, d)
        else:
            c, d = fadd(a, c), fadd(b, d)
    if (b > N):
        return c, d
    else:
        return a, b

fareyAttempts = []

Pi_ = (1/2 * nsum(lambda k: (1/(16 ** k)) * ((8/((8 * k) + 2)) + (4/((8 * k) + 3)) + (4/((8 * k) + 4)) - (1/((8 * k) + 7))), [0, inf], method = 'richardson'))
zeta3 = (1/2 * nsum(lambda n: ((((-1) ** n) * ((fac(2 * n)) ** 3) * ((fac(n + 1)) ** 6) * ((40885 * (n ** 5)) + (124346 * (n**4)) + (150160 * (n**3)) + (89888 * (n**2)) + (26629 * n) + 3116)) / (((n + 1) ** 2) * ((fac((3 * n) + 3)) ** 4))), [0, inf], method = 'richardson'))

g = fdiv(zeta3, (mpmath.power(Pi_, 3)))
f = farey(g, mp.dps * mp.prec)

e = -1

h = 99999

while True:

    if (abs(fsub(fdiv((fmul(100, zeta3)), (fmul((fdiv(f[0], f[1])), (mpmath.power(Pi_, 3))))), 100))) <= (mpmath.power(10,(e))):
        e -= 1
        print(f"Correct to 10^{e}")
        mp.dps += 1
        mp.prec += 1
        h += 1
    else:
        g = fdiv(zeta3, (mpmath.power(Pi_, 3)))
        if g in gAttempts:
            gAttempts.append(g)
            mp.dps += 1
        elif g not in gAttempts:
            gAttempts.append(g)
            f = farey(g, h * mp.dps * mp.prec)
            h = fmul(h, 2)
            if f in fareyAttempts:
                fareyAttempts.append(f)            
            elif f not in fareyAttempts:
                fareyAttempts.append(f)
                print(Fr(int(Integer(Float(str(f[0]), mp.dps))), int(Integer(Float(str(f[1]), mp.dps)))))
                
    if mp.dps % 1280 == 0:
        mp.prec = mp.prec * 3
        Pi_ = (1/2 * nsum(lambda k: (1/(16 ** k)) * ((8/((8 * k) + 2)) + (4/((8 * k) + 3)) + (4/((8 * k) + 4)) - (1/((8 * k) + 7))), [0, inf], method = 'direct'))
        zeta3 = (1/2 * nsum(lambda n: ((((-1) ** n) * ((fac(2 * n)) ** 3) * ((fac(n + 1)) ** 6) * ((40885 * (n ** 5)) + (124346 * (n**4)) + (150160 * (n**3)) + (89888 * (n**2)) + (26629 * n) + 3116)) / (((n + 1) ** 2) * ((fac((3 * n) + 3)) ** 4))), [0, inf], method = 'direct'))      
