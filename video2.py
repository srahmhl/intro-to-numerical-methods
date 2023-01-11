""" Video 2: Song Compression by FFT
Sarah Mahl
Intro to Numerical Methods
2/10/21 
https://publish.illinois.edu/augmentedlistening/tutorials/music-processing/tutorial-1-introduction-to-audio-processing-in-python/
https://notebooks.gesis.org/binder/jupyter/user/ipython-ipython-in-depth-jtfovizd/notebooks/binder/video2.ipynb#
https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html
https://stackoverflow.com/questions/2060628/reading-wav-files-in-python
https://www.dummies.com/programming/python/performing-a-fast-fourier-transform-fft-on-a-sound-file/

"""

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from IPython.display import Audio #IPython.display.Audio

r, w = open('good_day.wav', 'rb')

print('Sampling Frequency:', r)
Audio(w, rate=r)

compression = np.fft.fft(w) #or is ifft the compressed wave?
Audio(compression, rate=r)

plt.figure()
plt.plot(w, compression)
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.title('Wave of Good Days by SZA')
"""

import wave

filename = 'good_day.wav'
wave.open(filename, 'rb')
