#!/usr/bin/python -tt

def donuts(count):
  # +++your code here+++
  if count >= 10:
    return 'Number of donuts: many'
  return 'Number of donuts: %d' % (count)

def main():
  print donuts(10)

# Standard boilerplate to call the main() function.
if __name__=='__main__':
  main()  