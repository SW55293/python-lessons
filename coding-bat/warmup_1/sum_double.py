# -*- coding: utf-8 -*-
"""
Given two int values, return their sum.
Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""

def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  return a + b

print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))
print(sum_double(3, 3))
print(sum_double(0, 0))
print(sum_double(0, 1))
print(sum_double(3, 4))
print(sum_double(-1, 0))
