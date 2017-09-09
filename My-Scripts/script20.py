#!/usr/bin/env python -tt

# Import
import sys

def main():
  if len(sys.argv) != 1:
    # reading
    f = open(sys.argv[1], 'rU')
    '''
    print f.readlines()
    print '*' * 10
    '''
    s = f.read()
    print s
    f.close()
    del f

    f1 = open(sys.argv[2], 'w')
    f1.write(s)
    f1.close()
    f2 = open(sys.argv[2], 'rU')
    print '*' * 100
    for line in f2:
      print line,
    f2.close()  
  else:
    print 'No file specified'
    sys.exit(1)  
# Standard boilerplate for calling main  
if __name__ == '__main__':
  main() 