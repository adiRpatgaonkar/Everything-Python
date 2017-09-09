#!/usr/bin/env python -tt

'''
  Regular expressions : 
  Emails example!
  findall and Groups example!

  findall
  findall() is probably the single most powerful function in the re module. 
  Above we used re.search() to find the first match for a pattern. 
  findall() finds *ALL* the matches and returns them as a list of strings, with each string representing one match.
 
'''

# Import
import re

def main():
  emailID = 'czxswefdcds d qd patgaonkar.nivedita22@gmail.comccpsddvc adityapatgaonkar9@gmail.com'
  emails = re.findall(r'([\w.-]+)@([\w.]+com)', emailID) 

  if emails:
    print 'Found IDs:'
    for email in emails:
      print 'Username:', email[0]
      print 'Host:', email[1]
      print
  else:
    print 'Not found'

# Standard boilerplate for calling main()
if __name__ == '__main__':
  main()