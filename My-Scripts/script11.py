#!/usr/bin/env python -tt

# sorting with tuples & lists!

# Import modules

def CustomSort(name):
	return (len(name), name)

def main():
	a = ['Ameya', 'Aditya', 'Arushi']
	print sorted(a)

	t = []
	x = len(a)
	for i in range(x):
	  t.append(CustomSort(a[i]))
	print sorted(t)  
		
# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()
