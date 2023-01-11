""" HW1
Sarah Mahl
1/13/20
MATH 3450 """

import math
import random

def f(x):
    return math.sin(2*math.pi*math.cos(x))

def RER(a,b,N):
    deltax = (b-a)/N
    sum = 0.0
    x = b

    for i in range(N):
        sum += f(x)
        x -= deltax

    return deltax*sum

def TrapR(a,b,N):
    deltax = (b-a)/N
    sum = 0.0
    x = a

    for i in range(N-1):
        sum += f(x)
        x += deltax
    
    return deltax*(0.5*(f(a)+f(b))+sum)

def SimpR(a,b,N):
    deltax = (b-a)/N
    sum = 0.0
    x = a

    if N % 2 != 0: # N is odd
        raise ValueError("N must be even.")

    for i in range(1,N,2):
        sum += 4*f(x)
        x += deltax

    for j in range(2,N-1,2):
        sum += 2*f(x)
        x += deltax
    
    return (deltax/3)*(f(a)+f(b)+sum)

def MCInt(a,b,N):
    deltax = (b-a)/N
    sum = 0.0
    x = a

    for i in range(N):
        sum += f(random.uniform(a,b))
        x += deltax

    return deltax*sum

def f2D(x,y):
    return math.sin(x**2 + y**3)

def TrapR2D(a,b,c,d,Nx,Ny):
    deltax = (b-a)/Nx
    deltay = (d-c)/Ny
    sum_1 = 0.0
    sum_2 = 0.0
    sum_3 = 0.0
    sum_4 = 0.0
    sum_final = 0.0
    x = a
    y = c

    for i in range(Nx-1):
        sum_1 += f2D(x,c)
        sum_2 += f2D(x,d)
        x += deltax

    for j in range(Ny-1):
        sum_3 += f2D(a,y)
        sum_4 += f2D(b,y)
        y += deltay

    for i in range(Ny-1):
        for j in range(Nx-1):
            sum_final += f2D(x,y)
            x += deltax
        y += deltay

    return ((deltax*deltay)/4)*(f2D(a,c)+f2D(a,d)+f2D(b,c)+f2D(b,d)+2*(sum_1+sum_2+sum_3+sum_4)+4*sum_final)

def MCInt2D(a,b,c,d,Nx,Ny):
    deltax = (b-a)/Nx
    deltay = (d-c)/Ny
    sum = 0.0
    x = a
    y = c

    for i in range(Ny):
        for j in range(Nx):
            sum += f2D(random.uniform(a,b), random.uniform(c,d))
            x += deltax
        y += deltay

    return deltax*deltay*sum

def main():
    print(TrapR2D(0,1,2,3,10000,10000))
    print(MCInt2D(0,1,2,3,10000,10000))

if __name__ == "__main__":
    main()