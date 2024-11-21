import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from numpy.fft import fftshift, fft2, ifft2, ifftshift

plt.gray()
frequnoisy = imread('frequnoisy.tif').astype(np.float64)/255

fourier_frequnoisy = fftshift(fft2(frequnoisy))
mag_frequnoisy = np.abs(fourier_frequnoisy)

points = [[64, 64], [104, 118], [152, 138], [192, 192]] # points in (x, y)
for x, y in points:
    fourier_frequnoisy[y][x] = 0

plt.imshow(np.log(np.abs(fourier_frequnoisy)))
plt.show()

result = ifft2(ifftshift(fourier_frequnoisy))
plt.imshow(np.abs(result))
plt.show()
