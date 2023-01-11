""" Video 3: Parallel Coding with Python 
    Image Manipulation """

import multiprocessing as mp
import matplotlib.pyplot as plt
from PIL import Image
import time

entries = ['copycatkiller.jpg','funeral.jpg','ifwemakeitthroughdecember.jpg','motionsickness.jpg','punisher.jpg','strangerinthealps.jpg']

def displayimg(i):
    """ plots image, i, unchanged """
    p = plt.imshow(i, interpolation='antialiased') # ANTIALIAS = greatest quality of image possible
    x_axis = p.axes.get_xaxis()
    x_axis.set_visible(False)
    y_axis = p.axes.get_yaxis()
    y_axis.set_visible(False)
    return None

def displayimges(i):
    """ produces plots of image bands side by side """
    fig, axarr = plt.subplots(1,3) # 3 bands in an image
    axarr[0].imshow(i[0])
    axarr[1].imshow(i[1])
    axarr[2].imshow(i[2])
    return None

def parallel(img):
    """ parallel process for plotting the three bands of an image """
    image = Image.open(img)
    r,g,b = image.split()
    displayimg(r)
    plt.savefig("C:\\Users\\mahls\\OneDrive\\Desktop\\nummethods\\phoebe\\%s_shift_r.jpg" % img, pil_kwargs={'optimize':True})
    displayimg(g)
    plt.savefig("C:\\Users\\mahls\\OneDrive\\Desktop\\nummethods\\phoebe\\%s_shift_g.jpg" % img, pil_kwargs={'optimize':True})
    displayimg(b)
    plt.savefig("C:\\Users\\mahls\\OneDrive\\Desktop\\nummethods\\phoebe\\%s_shift_b.jpg" % img, pil_kwargs={'optimize':True})
    return None

if __name__ == "__main__":
    # serial processing
    start_time = time.time()
    for elem in entries:
        image = Image.open(elem)
        r,g,b = image.split()
        displayimg(r)
        plt.savefig("C:\\Users\\mahls\\OneDrive\\Desktop\\nummethods\\phoebe\\%s_shift_r.jpg" % elem, pil_kwargs={'optimize':True})
        displayimg(g)
        plt.savefig("C:\\Users\\mahls\\OneDrive\\Desktop\\nummethods\\phoebe\\%s_shift_g.jpg" % elem, pil_kwargs={'optimize':True})
        displayimg(b)
        plt.savefig("C:\\Users\\mahls\\OneDrive\\Desktop\\nummethods\\phoebe\\%s_shift_b.jpg" % elem, pil_kwargs={'optimize':True})
    print("%s seconds to run" % (time.time() - start_time))
    
    # parallel processing with Pool.map
    second_time = time.time()
    pool = mp.Pool(mp.cpu_count())
    pool.map(parallel,entries)
    pool.close()
    print("%s seconds to run" % (time.time() - second_time))