#!/usr/bin/env python
# import modules used here -- sys is a very standard one
import sys

def main():
    # Get the name from the command line
    print 'Hello there', sys.argv[1]
    
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
