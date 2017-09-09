#!/usr/bin/env python -tt

# Import

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
  return sorted(list1 + list2)

def main():
  l1 = ['aa', 'xx', 'zz']
  l2 = ['bb', 'cc']
  print linear_merge(l1, l2)

# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()  