#!/usr/bin/env python -tt

# Various lists' operations

# Import modules

def main():
  a = [1, 4, 5, 2, 8]
  print 'a =', a, '\nlength of a is', len(a)
  a = a + [7, 4]
  print 'a modified to', a
  
  b = a # b points to the same list as a. b is NO COPY of a
  print 'b = ', b
  c = a[:] # c is a new COPY of a
  print 'c = ', c
  a[0] = 0
  print 'a modified to', a
  print 'b = ', b
  print 'c = ', c
  
# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()  
   