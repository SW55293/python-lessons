# -*- coding: utf-8 -*-
"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""
def array_front9(nums):
  firstFour = nums[:4]
  for n in firstFour:
    if n == 9:
      return True
  return False


print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1, 2, 3, 4, 5]))
print(array_front9([3, 9, 2, 3, 3]))
print(array_front9([9, 2, 3]))
print(array_front9([1, 9, 9]))
print(array_front9([1, 2, 3]))
print(array_front9([1, 9]))
print(array_front9([5, 5]))
print(array_front9([2]))
print(array_front9([9]))
print(array_front9([]))
