#!/usr/bin/env python -tt

# Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
  fileName = 'SIP_4.jpg'

  img = cv2.imread(fileName, 0)
  reso = img.shape
  print reso
  #img = img[:, :, :: -1]
  print img
  lowThres = 60
  ratio = 3 # 3:1
  highThres = lowThres * ratio
  up = []
  low = []
  for i in range(reso[0]):
    for j in range(reso[1]):
      if img[i][j] > highThres:
        up.append(img[i][j])
      elif img[i][j] < lowThres:
        low.append(img[i][j])
  print up
  print low    
  plt.imshow(img)
  plt.show()

if __name__ == '__main__':
  main()
