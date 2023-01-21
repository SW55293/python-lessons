# -*- coding: utf-8 -*-
"""
Given an int n, return the absolute difference between n and 21, 
except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""

def diff21(n):
  while n <= 21:
    return 21 - n
  return (n - 21) * 2


print(diff21(10))
print(diff21(21))
print(diff21(19))
print(diff21(22))
print(diff21(25))
print(diff21(30))
print(diff21(0))
print(diff21(1))
print(diff21(2))
print(diff21(-1))
print(diff21(-2))
print(diff21(50))