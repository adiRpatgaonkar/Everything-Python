#!/usr/bin/env python -tt

# Import
import sys

def HashKeyElem(dict, key):
  if key in dict:
    return dict[key]
  else:
    return "This key doesn't exist"  


def main():
  if len(sys.argv) != 2:
    print 'Usage:$python xxx.py keyName'
    sys.exit(1)
  hashT = {}
  hashT['a'] = ['Aditya']
  hashT['a'].append('Ameya')
  hashT['b'] = 'Shriyaan'
  print HashKeyElem(hashT, sys.argv[1])
  print hashT.get(sys.argv[1]),'(USING hashT.get(keyName) function)'

# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()