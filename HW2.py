""" HW2
Sarah Mahl
1/22/21 """

import math
import cmath
import numpy as np

def f(x):
    #return x**5.0-2.0
    #return math.e**x-3.0*x**2.0
    return x-math.tan(x)

def Df(x): # derivative of f(x)
    #return 5.0*x**4.0
    #return math.e**x-6.0*x
    return 1.0-(1/math.cos(x)**2.0)

def Bisection(a,b,N):
    """ Bisection method for rootfinding
    Takes boundaries a,b with N iterations """
    for i in range(1,N+1):
        c = (1/2)*(a+b)
        if f(a)*f(c) > 0.0:
            a = c
        else:
            b = c
    return c

def Newton(x0,N):
    """ Newton method for rootfinding
    x0 is the initial guess, method iterates N times """
    x_next = x0
    for i in range(0,N):
        f_n = f(x_next)
        if Df(x0) == 0:
            return ValueError("No solution.")
            break
        else:
            derivf = Df(x_next)
            x_next = x_next - f_n/derivf
    return x_next

def F(x):
    """ function definition for a system of equations,
    x is the vector [x_1,x_2,...,x_n] """
    return [x[0]**2.0+x[1]**2.0-2.0*x[0]-2.0*x[1]+1.0,x[0]+x[1]-2.0*x[0]*x[1]]

def DF(x):
    """ Jacobian definition for a system of equations 
        J = [[DF1/dx1, DF1/dx2, DF1/dx3, ... , DF1/dxn]
             [DF2/dx1, DF2/dx2, DF2/dx3, ... , DF2/dxn]
                .         .        .             .
                .         .        .             .
                .         .        .             .
             [DFn/dx1, DFn/dx2, DFn/dx3, ... , DFn/dxn]] """
    return [[2.0*x[0]-2.0,2.0*x[1]-2.0],[1-2.0*x[1],1-2.0*x[0]]]

def NewtonVec(x0,N):
    """ Newton's method for any system of equations """
    inverseJ = np.linalg.inv(DF(x0))
    x_next = x0
    for i in range(0,N):
        F_n = F(x_next)
        x_next = x_next - inverseJ*F_n
        inverseJ = np.linalg.inv(DF(x_next))
    return x_next

def main():
    #print(NewtonVec([-1.0,1.0],10))
    #print(F([-1.0,1.0]))
    #print(DF([-1.0,1.0]))

    print(Newton(100,100))

if __name__ == "__main__":
    main()