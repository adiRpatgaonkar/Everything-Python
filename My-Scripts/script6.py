#!/usr/bin/python -tt

#import modules

def main():
  a = [1, 5, 2, 4]
  for num in a:
    print num
  print 'Length of list is', len(a)
  a.append(10)
  print a
  print 'Is 10 in list a?\n', (10 in a)
  a.pop(-1)
  print 'Is 10 in list a?\n', (10 in a)
  del a
  print a # Won't work

# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()