#!/usr/bin/python -tt

#import modules

def MixUp(a, b):
  return b[0:2] + a[2:] + ' ' + a[0:2] + b[2:]

def main():
  print MixUp('dog', 'dinner')

# Standard boilerplate to call the main() function.
if __name__=='__main__':
  main()
