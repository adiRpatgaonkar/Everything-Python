#!/usr/bin/env python -tt

# Import

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

def LastElem(tuple):
	return tuple[1]

def sort_last(tuples):
  # +++your code here+++
  return sorted(tuples, key = LastElem) 

def main():
  tuples = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
  print sort_last(tuples)

# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()  