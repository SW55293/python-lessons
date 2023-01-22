# -*- coding: utf-8 -*-
"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False	
makes10(1, 9) → True
makes10(10, 1) → True
makes10(10, 10) → True
makes10(8, 2) → True
makes10(8, 3) → False	
makes10(10, 42) → True
makes10(12, -2) → True
"""

def makes10(a, b):
  if (a == 10 or b == 10 or a + b == 10):
    return True
  return False



#a = 10 return true
#b = 10 return true
#if a + b = 10 return true

print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))
print(makes10(10, 1))
print(makes10(10, 10))
print(makes10(8, 2))
print(makes10(8, 3))
print(makes10(10, 42))
print(makes10(12, -2))