# -*- coding: utf-8 -*-
"""
Given 2 int values, return True if one is negative and one 
is positive. Except if the parameter "negative" is True, then 
return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""

def pos_neg(a, b, negative):
  if ((a < 0 and b < 0) and (negative == True)):
    return True
  elif ((a < 0 and b < 0) and (negative == False)):
    return False
      
  while (a < 0 or b < 0):
    if negative == False:
      return True
    elif negative == True:
      return False
      
  return False
    

# if a or b is negative return true
# if both are negative and negative = True return False
# if both a and b are negative

  #     
  # elif ((a < 0 or b < 0) and (negative == True)):
  #   return False
  # elif ((a < 0 or b < 0) and (negative == True)):
  # return True
	
print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
print(pos_neg(-4, -5, False))
print(pos_neg(-4, 5, False))
print(pos_neg(-4, 5, True))
print(pos_neg(1, 1, False))
print(pos_neg(-1, -1, False))
print(pos_neg(1, -1, True))
print(pos_neg(-1, 1, True))
print(pos_neg(1, 1, True))
print(pos_neg(-1, -1, True))	
print(pos_neg(5, -5, False))	
print(pos_neg(-6, 6, False))	
print(pos_neg(-5, -6, False))	
print(pos_neg(-2, -1, False))	
print(pos_neg(1, 2, False))	
print(pos_neg(-5, 6, True))	
print(pos_neg(-5, -5, True))