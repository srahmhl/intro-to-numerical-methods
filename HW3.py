""" HW3
Sarah Mahl
Intro to Numerical Methods
1/29/21 """

import numpy as np
#import scipy
import time

def Jacobi(A,b,x0,iterations,tol):
    """ A is an nxn square matrix;
    b is a vector of size n;
    x0 is the initial guess, a vector of size n """

    for i in range(iterations+1):
        x = x0.copy()
        for j in range(len(x)):
            for l in range(len(x)):
                if l != j:
                    x0[j] = (1/A[j][j])*(b[j]-np.sum(A[j][l]*x[l]))
                    #print("x:", x0)
        if np.linalg.norm(np.subtract(x,x0)) < tol:
            print("Converging within", tol, "by Jacobi found after", i, "iterations.")
            return x0
    print("Solution after", iterations, "iterations of the Jacobi method. Did not converge within", tol)
    return x0

def GaussSeidel(A,b,x0,iterations,tol):
    """ iterative method to solve Ax = b, where A = N - P, N and P are both matrices;
    N is the upper triangular of A, P is the lower triangular of A;
    x0 is the initial guess for the solution """

    x = x0.copy()
    N = np.triu(A)
    P = np.subtract(N,A)
    for i in range(iterations):
        x = np.dot(np.linalg.inv(N),(b+np.dot(P,x)))
        if np.linalg.norm(np.subtract(x0,x)) < tol:     # if np.linalg.norm(np.dot(np.linalg.inv(N),P)) < tol ?
            print("Converging within", tol, "by Gauss-Seidel found after", i, "iterations.")
            return x
    print("Solution by Gauss-Seidel not found in", iterations, "iterations. Did not converge within", tol)
    return x

def main():
    """ Ax = (a*I + R)x = b where a is a positive constant, I is an NxN identity matrix, 
    and R is an NxN matrix of uniformly distributed random numbers between 0 and 1. 
    Also reading in data for Wx=p. """

    """ Number 2: """
    N = 22
    a = 2
    I = np.identity(N)
    R = np.random.rand(N,N) # default low is 0.0 and default high is 1.0, NxN is the size of the matrix
    A = a*I + R
    b_empty = []
    for n in range(1,N+1):
        b_empty.append(n)
    b = np.transpose(b_empty) 
    x = np.random.rand(N)

    print(Jacobi(A,b,x,20,0.00000001))
    print(GaussSeidel(A,b,x,20,0.00000001))

    """ Number 3:
    W = np.loadtxt('W.out')
    p = np.loadtxt('p.out')
    N = len(p)
    x = np.random.rand(N) # initial guess is a matrix of size N of random numbers between 0 and 1
    start_time = time.time()
    print(Jacobi(W,p,x,20,0.00000001))
    print(GaussSeidel(W,p,x,20,0.00000001))
    #print("LU Decomp:", scipy.linalg.lu(W))
    print("Inverse of W:", np.linalg.inv(W))
    print("Backslash operator:", np.linalg.solve(W,p))
    end_time = time.time()
    print(" %s seconds" % (end_time - start_time)) """

def main2():
    """ example from class """
    A = [[10,3,1],[2,-10,3],[1,3,10]]
    b = [14,-5,14]
    x = [0,0,0]
    print(Jacobi(A,b,x,20,0.00000001))
    print(GaussSeidel(A,b,x,20,0.00000001))

if __name__ == "__main__":
    main()