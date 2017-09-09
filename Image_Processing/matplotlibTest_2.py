#!/usr/bin/env python -tt

# Import
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
  fileName = 'SIP_4.jpg'

  imgCV = cv2.imread(fileName, -1)
  plt.subplot(121)
  plt.imshow(imgCV)

  '''
  #More comprehensive way
  (b, g, r) = cv2.split(imgCV)
  imgMat = cv2.merge((r, g, b))

  '''
  imgMat = imgCV[:, :, :: -1]
  plt.subplot(122)
  plt.imshow(imgMat)
  plt.show()  

if __name__ == '__main__':
  main()