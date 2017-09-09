#!/usr/bin/env python -tt

'''
  Basic regular expressions example!
'''

# Import
import re

def main():
  '''
  Search for ooo in string stri
  All of the pattern must match, but it may appear anywhere.
  On success, match.group() is matched text.
  '''
  stri = 'What have I dooone? Oh myyy god! covfef122e @acbd'
  ##match = re.search(r'ooo', stri)
  ##match = re.search(r'.ooo...', stri)
  match = re.search(r'\w\w\w\d\d\d\w', stri)
  if match:
    print 'Found', match.group()
  else:
    print 'Not found'  

# Standard boilerplate for calling main()
if __name__ == '__main__':
  main()