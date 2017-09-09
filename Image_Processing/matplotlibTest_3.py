#!/usr/bin/env python -tt

# Import
import numpy as np
from matplotlib import pyplot as plt

def main():
  x = np.arange(0, 10, 0.001)
  y = np.sin(x)
  plt.plot(x, y)
  plt.show()

if __name__ == '__main__':
  main()