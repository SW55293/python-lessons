# -*- coding: utf-8 -*-
"""

Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""
def near_hundred(n):
  if n < 0: return False
  num = abs(n)
  if num >= 90 and num <= 110:
    return True
  elif num >= 190 and num <= 210:
    return True
  return False
  

# 110-100 and 90-100
# 210-200 and 190-200

# if ((abs(n) >= 90 and abs(n) <= 110) or (abs(n) >= 190 and abs(n) <= 210)):
#     return True
    
#   return False

print(near_hundred(93))	
print(near_hundred(90))	
print(near_hundred(89))
print(near_hundred(110))
print(near_hundred(111))
print(near_hundred(121))
print(near_hundred(-101))
print(near_hundred(-209))
print(near_hundred(190))
print(near_hundred(209))
print(near_hundred(0))
print(near_hundred(5))
print(near_hundred(-50))	
print(near_hundred(191))	
print(near_hundred(189))	
print(near_hundred(200))	
print(near_hundred(210))	
print(near_hundred(211))
print(near_hundred(290))