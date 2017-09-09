#!/usr/bin/env python -tt

# Import

# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

def match_ends(words):
  # +++your code here+++
  x = len(words)
  count = 0
  for i in range(x):
  	if (len(words[i]) >= 2) and (words[i][0].lower() == words[i][-1].lower()):
  		count += 1
  return count

def main():
	stringList = ['Aditya', 'Ameya', 'Aarusha']
	print match_ends(stringList)

# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()