#!/usr/bin/env python -tt

# For loops

# Import modules


def main():
	a  = range(20)

	for i in range(0, 20, 2):
		print a[i]

	for i in range(1, 20, 2):
		print a[i]

	for i in a:
		a.append(i)
	print a		

# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()
