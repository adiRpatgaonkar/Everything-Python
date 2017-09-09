#!/usr/bin/env python -tt

# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
  fileName = 'BerkeleyTower.png'

  img = cv2.imread(fileName, -1)
  print img.shape
  print img.size
  print img.dtype

  img = img[:, :, :: -1]

  redB = np.copy(img)
  redB[:, :, 2] = 0
  redB[:, :, 1] = 0

  enhRed = np.copy(img)
  enhRed[:, :, 0] *= 2
  plt.subplot(311)
  plt.imshow(img)
  plt.subplot(312)
  plt.imshow(enhRed)
  plt.subplot(313)
  plt.imshow(redB)
  plt.show()

if __name__ == '__main__':
  main()  