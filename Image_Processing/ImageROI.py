#!/usr/bin/env python -tt

# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
  fileName = 'SIP_4.jpg'

  img = cv2.imread(fileName, -1)
  img = img[:, :, :: -1]
  roi = np.copy(img)
  roi = img[650:750, 800:1000]
  img[400:500, 200:400] = roi
  plt.imshow(img)
  plt.show()

if __name__ == '__main__':
  main()
