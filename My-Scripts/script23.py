#!/usr/bin/env python -tt

'''
  Basic regular expressions example!
'''

# Import
import re


def main():
  stri = 'Hwello, howdy. You\'vee-v got:guts I\'ll give you that'
  match = re.search(r'\'\w\w\w\b-\b\w\s', stri)
  if match:
    print 'Found', match.group()
  else:
    print 'Not found'  

# Standard boilerplate for calling main()
if __name__ == '__main__':
  main()
