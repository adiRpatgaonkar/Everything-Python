#!/usr/bin/env python -tt

# Imports
import sys

# Remove ##s only for DEBUGGING!

def SortedHash(tuple):
  return tuple[1]

def TopCount(fileVar):
  wordCountDict = {}
  for line in fileVar:
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
  # Got the hint of putting the hash table in a list of tuples from STACK OVERFLOW
  # Thank you, Adam & Devin Jeanpierre!
  wordCountDictS = sorted(wordCountDict.items(), key = SortedHash, reverse = True) 
  for elem in wordCountDictS:
    print elem[0].encode('string-escape'), '>', elem[1]
  return

def WordCount(fileVar):
  wordCountDict = {}
  for line in fileVar:
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
  ##print wordCountDict
  for key in wordCountDict.keys():
    print key.encode('string-escape'), '>', wordCountDict[key]  
  return

def main():
  argc = len(sys.argv)
  if argc == 2 or argc == 3:
    fileName = sys.argv[1]
    f = open(fileName, 'rU')

    if argc == 3:
      option = (sys.argv[2]).lower()
      if option == '--count':
        WordCount(f)
      elif option == '--topcount':
        TopCount(f)
      else:
        print 'Invalid option.\nUsage:python progName.py filename.txt {--count | --topcount}'
        f.close()
        sys.exit(1) 
    else:
      for line in f:
        print line,
         
    f.close()        
  else:
    print 'Usage:python progName.py filename.txt {--count | --topcount}'
    sys.exit(1)

# Standard boilerplate for calling main()
if __name__ == '__main__':
  main()
