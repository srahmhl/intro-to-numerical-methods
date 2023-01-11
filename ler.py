# left-endpoint rule for numerical integration

import math

def f(x):
    return math.exp(x)

def LER(a,b,N):
    deltax = (b-a)/N
    sum = 0.0
    x = a

    for j in range(N-1):
        sum += f(x)
        x += deltax

    return deltax * sum

def main():
    print(LER(0,math.pi,100))

if __name__ == "__main__":
    main()

# can add an array of N = [10, 10**2, 10**3, ...] and have LER iterate through it in main() to show how the approximation gets better
# can then make a table for error
# edit output for readability