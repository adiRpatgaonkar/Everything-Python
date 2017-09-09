#!/usr/bin/env python -tt

# Joining and appending

# Import modules

def main():
  a = ['a', 'bb', 'ccc', 'dddd']
  a = '\n'.join(a)
  print "a is \n", a

  b = a.split('\n')
  print "b is", b

  result = []
  for num in b:
  	result.append(num)
  print 'result is', result
  
# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()
