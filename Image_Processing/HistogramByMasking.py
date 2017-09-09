#!/usr/bin/env python -tt
# HistogramByMasking.py

# Imports

import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():

  if len(sys.argv) > 1:
    fileName = sys.argv[1]
    img = cv2.imread(fileName, 0)
    reso = img.shape
    rowDim1 = 0
    rowDim2 = reso[0]
    colDim1 = 0
    colDim2 = reso[1]

    if len(sys.argv) == 3 and sys.argv[2] == '--tomask':
      print 'Please input the row dimensions: '
      rowDim1, rowDim2 = raw_input().split(":")
      print 'Please input the column dimensions: '
      colDim1, colDim2 = raw_input().split(":")
      rowDim1 = int(rowDim1)
      rowDim2 = int(rowDim2)
      colDim1 = int(colDim1)
      colDim2 = int(colDim2)

    #print img.shape[:2]
    mask = np.zeros(img.shape[:2], np.uint8)
    #print mask

    mask[rowDim1:rowDim2, colDim1:colDim2] = 255

    '''
    masked_img = np.empty_like(img)
    print img[100:668, 100:1266]
    masked_img[100:668, 100:1266] = img[100:668, 100:1266]

    '''
    masked_img = cv2.bitwise_and(img, img, mask = mask)

    hist_full = cv2.calcHist([img], [0], None, [256], [0,256])
    hist_masked = cv2.calcHist([img], [0], mask, [256], [0,256])

    plt.subplot(2, 2, 1), plt.imshow(img, 'gray')
    plt.subplot(2, 2, 2), plt.imshow(mask, 'gray')
    plt.subplot(2, 2, 3), plt.imshow(masked_img, 'gray')
    plt.subplot(2, 2, 4), plt.plot(hist_full, 'r'), plt.plot(hist_masked, 'g')
    plt.xlim([0, 256])
    plt.show()
  else:
    print 'Usage: python prog.py filename [--tomask]'
    sys.exit()

if __name__ == '__main__':
  main()