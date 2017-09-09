#!/usr/bin/env python -tt

# Imports
import cv2
import numpy as np # Giving a module a different alias


def main():
  # Loading a color image in grayscale
  '''
    cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag: 1
    cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode: 0
    cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel: -1
  '''
  img = cv2.imread('SIP_1.jpg', 1)
  print img # If path is wrong, NO ERROR. However none will be returned

  cv2.imshow('Gray Image', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()