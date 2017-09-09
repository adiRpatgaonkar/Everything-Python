#!/usr/bin/env python -tt

'''
  Regular expressions : 
  Emails example! 
  Sqaure brackets usage example!
  Groups example!
  
  (More square-bracket features) You can also use a dash to indicate a range, so [a-z] matches all lowercase letters. 
  To use a dash without indicating a range, put the dash last, e.g. [abc-]. 
  An up-hat (^) at the start of a square-bracket set inverts it, so [^ab] means any char except 'a' or 'b'.

'''

# Import
import re

def main():
  emailID = 'czxswefdcds d qd patgaonkar.nivedita22@gmail.comccpsddvc'
  match = re.search(r'([\w.-]+)@([\w.]+com)', emailID) # match.group => adityapatgaonkar9@gmail

  if match:
    print 'Found ID:', match.group()
    print 'Username:', match.group(1)
    print 'Host:', match.group(2)
  else:
    print 'Not found'

# Standard boilerplate for calling main()
if __name__ == '__main__':
  main()