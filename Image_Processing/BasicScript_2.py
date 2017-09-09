#!/usr/bin/env python -tt

# Imports
import cv2
import numpy as np


def main():
  fileName = 'SIP_3.jpg'
  img = []
  x = 0
  for i in range(-1, 2):
    img.append(cv2.imread(fileName, i))
    cv2.namedWindow('Image'+str(x), cv2.WINDOW_NORMAL)
    cv2.imshow('Image'+str(x), img[x])
    x += 1

  k = cv2.waitKey(0) & 0xFF # For 64 bit machine 
  if k == 27:
    print 'Exiting without saving'
  elif k == ord('s'):
    grayImg = cv2.imread(fileName, 0)
    cv2.imwrite('graySIP_3.tif', grayImg)
    print 'Saving & exiting'    
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()  