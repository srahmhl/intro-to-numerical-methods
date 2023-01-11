""" HW6: Singular Value Decomposition
Sarah Mahl
March 10th, 2021
MATH 3450 Intro to Numerical Methods """

import numpy as np
import scipy.linalg as la
import math
from PIL import Image
import matplotlib.pyplot as plt

def MySVD(A):
    """ takes a real MxN matrix A and returns the singular value
    decomposition of A in the form of U, Sigma, and V """

    A = np.array(A)
    A_star = np.transpose(A)
    eigenDecompRight = la.eig(A @ A_star)
    eigenDecompLeft = la.eig(A_star @ A)
    
    # make U
    eigenvectorsRight = eigenDecompRight[1]
    U = []
    for vector in eigenvectorsRight:
        magnitude = la.norm(vector)
        vector = vector / magnitude
        U.append(vector)

    # make V
    eigenvectorsLeft = eigenDecompLeft[1]
    V = []
    for vector in eigenvectorsLeft:
        magnitude = la.norm(vector)
        vector = vector / magnitude
        V.append(vector)

    # make Sigma
    singularvalues = eigenDecompLeft[0]
    for eval in range(len(singularvalues)):
        singularvalues[eval] = math.sqrt(singularvalues[eval])
    Sigma = np.diag(np.real(singularvalues))

    return U, Sigma, np.transpose(V)

def MyTruncatedSVD(A,s):
    """ takes a real MxN matrix A and a real number s, returns the
    SVD approximation of A where all singular values less than s
    (and associated singular vectors) have been deleted """
    
    A = np.array(A)
    A_star = np.transpose(A)
    eigenDecompRight = la.eig(A @ A_star)
    eigenDecompLeft = la.eig(A_star @ A)
    
    # U
    eigenvectorsRight = eigenDecompRight[1]
    U = []
    for vector in eigenvectorsRight:
        magnitude = la.norm(vector)
        vector = vector / magnitude
        U.append(vector)

    # V
    eigenvectorsLeft = eigenDecompLeft[1]
    V = []
    for vector in eigenvectorsLeft:
        magnitude = la.norm(vector)
        vector = vector / magnitude
        V.append(vector)

    # Sigma
    singularvalues = eigenDecompLeft[0]
    for eval in range(len(singularvalues)):
        singularvalues[eval] = math.sqrt(singularvalues[eval])
    Sigma = np.diag(np.real(singularvalues))

    #exvar = np.real(singularvalues)**2.0/np.sum(np.real(singularvalues)**2.0)
    #exvar = exvar[0:32]
    #x = list(range(1,33))
    #plt.scatter(x, exvar, color='b')
    #plt.title('Significant Singular Values')
    #plt.xlabel('Explained Variance')
    #plt.show()

    # truncation
    newSigma = Sigma.copy()
    low_vals = newSigma < s
    newSigma[low_vals] = 0
    # issue with image output could be here, but this works to cut out singular values less than s
    # though it doesn't delete the associated singular vectors because this change the size of the
    # Sigma matrix and prevented multiplication when multiplying U, Sigma, and V later on

    return U, newSigma, np.transpose(V)

def MyTruncatedSVDImage(filename, s):
    """ takes an image file and a real number s, creates the
    SVD approximation in which all singular values less than
    s and (and associated singular vectors) have been deleted """
    
    img = Image.open(filename)
    r,g,b = img.split()
    # the issue could also be with the split() function, though manually reading in arrays for the
    # red, green, and blue bands using for loops with the data from img took too long to be feasible
    red_band = np.array(r, float) / 255
    green_band = np.array(g, float) / 255
    blue_band = np.array(b, float) / 255

    rU,rS,rV = MyTruncatedSVD(red_band,s)
    gU,gS,gV = MyTruncatedSVD(green_band,s)
    bU,bS,bV = MyTruncatedSVD(blue_band,s)
    
    redSVD = rU @ rS @ rV
    greenSVD = gU @ gS @ gV
    blueSVD = bU @ bS @ bV

    img_approx = np.dstack((redSVD,greenSVD,blueSVD))
    # the issue could also be here with the np.dstack function, since this
    # combines the new red, green, and blue bands back into the approximated image
    # but i'm not sure why that would have gone wrong unless i'm using the wrong method/function

    p = plt.imshow(img_approx)
    x_axis = p.axes.get_xaxis()
    x_axis.set_visible(False)
    y_axis = p.axes.get_yaxis()
    y_axis.set_visible(False)
    plt.show()
    
    return img_approx

if __name__ == "__main__":
    A = [[-2,0],[2,-2],[0,2]]
    #MySVD(A)
    #print(MyTruncatedSVD(A,3))
    MyTruncatedSVDImage('punisher.jpg',0.1)