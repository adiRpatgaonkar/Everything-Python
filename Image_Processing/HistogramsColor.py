#!/usr/bin/env python -tt

# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():

  print 'Input the image name including the extension.'
  fileName = ''
  fileName = raw_input(fileName)

  img = cv2.imread(fileName, -1)
  img = img[:, :, :: -1]
  plt.subplot(222)
  plt.imshow(img, interpolation = 'bicubic')

  # Plot histogram using amtplotlib
  grayImg = cv2.imread(fileName, 0)
  plt.subplot(221)
  plt.imshow(grayImg, cmap = 'gray', interpolation = 'bicubic')
  plt.subplot(223)
  plt.hist(grayImg.ravel(), 256, [0, 256])
  plt.xlim([0, 256])
  
  # Plot histogram using openCV
  color = ('b', 'g', 'r')

  for i, col in enumerate(color):
    print i, col
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.subplot(224)
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
  plt.show()

if __name__ == '__main__':
  main()  