#!/usr/bin/python -tt

#import modules

def ReplaceSubString(s):
  r = s[0]
  x = s.replace(s[0], '*')
  return r + x[1:]

def main():
	print ReplaceSubString('babble')


# Standard boilerplate to call the main() function.
if __name__=='__main__':
	main()