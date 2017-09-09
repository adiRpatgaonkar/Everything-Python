#!/usr/bin/env python -tt

# Imported modules

import sys

def main():
  print sys.argv # Prints all the command line arguments
  print 'I am' , sys.argv[1] # When , is used for concatenating a space is attached b/w the 2 strings
  print 'I am originally from ' + sys.argv[2] # When + is used for concatenating a space is attached b/w the 2 strings 


# Standard boilerplate to call the main() function.
if __name__=='__main__':
  main()

