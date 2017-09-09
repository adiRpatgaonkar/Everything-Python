#!/usr/bin/env python -tt

#Import

import sys
import re


def main():
  if len(sys.argv) == 2:
    fileName = sys.argv[1]
    f = open(fileName, 'rU')
    rankDict = {}
    for line in f:
      match = re.search(r'Popularity in (\d\d\d\d)', line)
      if match:
        year = match.group(1)
      match = re.search(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', line)
      if match:
        if (match.group(2) not in rankDict) or ((match.group(2) in rankDict) and (match.group(1) < rankDict[match.group(2)])):
          rankDict[match.group(2)] = match.group(1)
        if (match.group(3) not in rankDict) or ((match.group(3) in rankDict) and (match.group(1) < rankDict[match.group(3)])):  
          rankDict[match.group(3)] = match.group(1)
    rankDict = sorted(rankDict.items())
    result = []
    result.append(year)
    for tuple in rankDict:
      print tuple[0], '>', tuple[1]
      result.append(tuple[0] + ' ' + tuple[1]) 
    print result
    f.close()
if __name__ == '__main__':
  main()