#!/usr/bin/env python -tt

# Import
import sys


def main():
  hashT = {}
  hashT['a'] = ['Aditya']
  hashT['a'].append('Ameya')
  hashT['b'] = 'Shriyaan'
  hashT['c'] = ['Vedang', 'Tej']
  hashT['d'] = ['Rajesh', 'Nilesh', 'Rupesh']

  ## Print all keys  
  for key in hashT.keys():
    print key
  ## Get keys' list
  keysL = hashT.keys()
  print keysL
  ## Get keys' values
  keyValuesL = hashT.values()
  print keyValuesL

  ## Looping over keys in sorted order
  hashTableSorted = sorted(hashT)
  for key in hashT.keys():
    print key, '>', hashT[key]

  ## Dictionary formatting
  print "%(a)s, %(b)s, %(c)s are all brothers" % hashT
  print "The children of Mak & Preeti are %(c)s" % hashT
  
# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()