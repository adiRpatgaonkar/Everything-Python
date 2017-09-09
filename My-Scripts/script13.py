#!/usr/bin/env python -tt

# Import

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  # +++your code here+++
  x = len(words)
  tempList = []
  tempList1 = []
  for i in range(x):
  	if words[i][0].lower() == 'x':
  		tempList.append(words[i])
  	else:
  		tempList1.append(words[i])
  toreturn = sorted(tempList) + sorted(tempList1)			
  return toreturn

def main():
	stringList = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
	print front_x(stringList)  

# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()  