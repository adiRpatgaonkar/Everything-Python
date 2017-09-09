#!/usr/bin/env python -tt

# Import

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  i = 0
  while i < (len(nums) - 1):
  #   DEBUGGING	
  ##	print 'i =', i, 'len =', len(nums) - 1
  ##	print nums[i], nums[i + 1]
  	while (i < len(nums) - 1) and (nums[i] == nums[i + 1]):
  	  nums.pop(i + 1)
  ##	print nums
  	i += 1  
  return nums

def main():
  list1 = [1, 2, 2, 3]
  print remove_adjacent(list1)

# Standard boilerplate for calling main  
if __name__ == '__main__':
  main()  