""" Video 3: Parallel Coding with Python 
    Simple Coding Example """

import multiprocessing as mp
import numpy as np
import time

def f(x):
    return x*x

def f_serial(x):
    """ x is an array """
    f = []
    for i in x:
        f.append(i**2)
    return f

if __name__ == "__main__":
    # Parallel processing
    start_time = time.time()
    pool = mp.Pool(mp.cpu_count())
    print(pool.map(f, [1,2,3]))
    pool.close()
    print("%s seconds to run" % (time.time() - start_time))

    # Serial processing
    second_time = time.time()
    print(f_serial([1,2,3]))
    print("%s seconds to run" % (time.time() - second_time))

