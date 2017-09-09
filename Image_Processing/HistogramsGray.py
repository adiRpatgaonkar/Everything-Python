#!/usr/bin/env python -tt

# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():

  fileName = ''
  fileName = raw_input(fileName)

  img = cv2.imread(fileName, 0)
  
  print img

  # hist = cv2.calcHist([image_name], [index_value], mask, [Num of bins], [range])
  hist = cv2.calcHist([img], [0], None, [256], [0, 256])

  plt.plot(hist)
  plt.xlim([0, 256])
  plt.show()

if __name__ == '__main__':
  main()  