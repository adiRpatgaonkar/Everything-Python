#!/usr/bin/env python -tt

'''
  Basic regular expressions: Repitition example!
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
  match = re.search(r'y+\s\w*\W', stri)
  stri2 = 'xx1      2    3xxx'
  match2 = re.search(r'\w*\d\s*\d\s*\d\w*', stri2)

  ## ^ = matches the start of string, so this fails:
  match3 = re.search(r'^b\w+', 'foobar')
  ## but without the ^ it succeeds:
  match4 = re.search(r'b\w+', 'foobar')
  
  if match3:
    print 'Found', match3.group()
  else:
    print 'Not found'  

# Standard boilerplate for calling main()
if __name__ == '__main__':
  main()