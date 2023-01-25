# -*- coding: utf-8 -*-
"""

Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""
def array_count9(nums):
  count = 0
  for n in range(len(nums)):
    if nums[n] == 9:
      count = count + 1
  return count

"""
You can also use this for loop

  for n in nums:
    if n == 9:
      count += 1
  return count
"""
print(array_count9([4, 2, 4, 3, 1]))
print(array_count9([9, 2, 4, 3, 1]))
print(array_count9([1, 9, 9, 3, 9]))
print(array_count9([1, 2, 3]))
print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([]))
