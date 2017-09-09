#!/usr/bi/env python -tt

# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
  fileName = 'SIP_4.jpg'
  img = cv2.imread(fileName, -1)
  #plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
  plt.imshow(img, interpolation = 'bicubic')
  plt.xticks([]), plt.yticks([])
  plt.show()

  cv2.imshow('Org', img)
  cv2.waitKey()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()