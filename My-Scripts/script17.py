#!/usr/bin/env python -tt

# Import
import sys


def main():
  if len(sys.argv) != 1:
    f = open(sys.argv[1], 'rU')
    for line in f:
      print line,
    f.close()
  else:
    print 'No file specified'
    sys.exit(1) 
# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()