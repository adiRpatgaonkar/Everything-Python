#!/usr/bin/env python -tt

# Imports
import cv2
import numpy as np

def main():
  
  fileName = 'SIP_4.jpg'
  img = cv2.imread(fileName)
  print img
  print '\n\n'
  cv2.imshow('Org', img)

  redB = np.empty_like(img)
  redB[:] = img
  greenB = np.empty_like(img)
  greenB[:] = img
  blueB = np.empty_like(img)
  blueB[:] = img

  redB[:, :, 0:2] = 0
  greenB[:, :, 0] = 0
  greenB[:, :, 2] = 0
  blueB[:, :, 1:3] = 0

  cv2.imshow('Red', redB)
  cv2.imshow('Green', greenB)
  cv2.imshow('Blue', blueB)
  cv2.waitKey()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()