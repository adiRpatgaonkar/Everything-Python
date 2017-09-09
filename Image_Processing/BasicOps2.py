#!/usr/bin/env python -tt

# Imports
import cv2
import numpy as np

def main():

  fileName = 'SIP_4.jpg'
  img = cv2.imread(fileName)
  px = img.item(100, 100, 0)
  print px
  img.itemset((100, 100, 0), 200)
  print img.item(100, 100, 0)

if __name__ == '__main__':
  main() 