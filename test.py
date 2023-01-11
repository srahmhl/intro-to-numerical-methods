# https://medium.com/@rameshputalapattu/jupyter-python-image-compression-and-svd-an-interactive-exploration-703c953e44f6

from PIL import Image
import numpy as np
import scipy.linalg as la

def compressSVD(imagefile, k):
    read = Image.open(imagefile)
    img = np.array(read)
    U, S, V = la.svd(img)
