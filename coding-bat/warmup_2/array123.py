# -*- coding: utf-8 -*-
"""

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""
def array123(nums):
#   if len(nums) < 2:
#     return False

  for n in range(len(nums)-2):
    if nums[n] == 1 and (nums[n+1] == 2) and (nums[n+2] == 3):
      return True
  return False

"""
If we dont set the loop to go end before the last 2 numbers we get
Compile problems:
list index out of range
So we need to keep it to run and stop when it reaches the last two
""" 
print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))	
print(array123([1, 1, 2, 1, 2, 1]))
print(array123([1, 2, 3, 1, 2, 3]))
print(array123([1, 2, 3]))
print(array123([1, 1, 1]))
print(array123([1, 2]))
print(array123([1]))
print(array123([]))

str = "dog"
print(len(str)-1)