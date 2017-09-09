#!/usr/bin/env python -tt

# Tuples!

# Import modules

def main():
	a = (5, 3, 2, 6)
	print a
	print sorted(a)
	for i in a:
		print i,
	print ''	
	print a[0:]
		
# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()
