#!/usr/bin/env python -tt

# Imports
import sys

def SortedHash(tuple):
  return tuple[1]


def main():

  if len(sys.argv) == 2:
    f = open(sys.argv[1], 'rU')
    
    wordCountDict = {}
    for line in f:
      line = line.lower()
      lineSplit = line.split(' ')
      ## print lineSplit
      l = len(lineSplit)
      i = 0
      while (i < l): 
        ## print lineSplit[i],
        if lineSplit[i] in wordCountDict:
          ## print 'True!!!'
          wordCountDict[lineSplit[i]] += 1
        else:
          ## print 'False!!'
          wordCountDict[lineSplit[i]] = 1 
        i += 1 
    print           
    ## print wordCountDict
    ##for key in wordCountDict.keys():
      ##print key.encode('string-escape'), '>', wordCountDict[key]

    ## Got the hint of putting the hash table in a list of tuples from STACK OVERFLOW
    wordCountDictS = sorted(wordCountDict.items(), key = SortedHash, reverse = True) 
    for elem in wordCountDictS:
      print elem[0].encode('string-escape'), '>', elem[1]     

    f.close()        
  else:
    print 'Usage:python progName.py filename.txt'

# Standard boilerplate for calling main()
if __name__ == '__main__':
  main()
