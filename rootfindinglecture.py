# Newton's Method

def f(x):
    return x^2-2

def df(x):
    return 2*x

def NewtonsMethod(x,N): # x is the initial guess
    x_n = x
    derivf = df(x_n)
    
    if derivf == 0:
        return ValueError("Derivative of f(x) cannot be zero.")

    zero = x_n - f(x_n)/derivf # want f(x) to be 0

    return zero