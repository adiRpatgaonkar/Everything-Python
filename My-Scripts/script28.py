#!/usr/bin/env python -tt

'''
  Regular expressions : 
  Files example!
 
'''

# Import
import re
import sys

def main():
  if len(sys.argv) == 2:
    f = open(sys.argv[1], 'rU')
    stri = f.read()
    stri = stri.lower()
    listMatch = re.findall(r'the\s\w+', stri)
    for elem in listMatch:
      print elem
    print len(listMatch), 'matches'  
  else:
    print 'Usage:python prog.py filename'    


# Standard boilerplate for calling main()
if __name__ == '__main__':
  main()