# -*- coding: utf-8 -*-
"""

Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. Return a 
new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""
def front3(str):
  if len(str) <= 3:
    return str * 3
  
  first_3 = str[0:3]
  return first_3 * 3

print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))
print(front3('abcXYZ'))
print(front3('ab'))
print(front3('a'))
print(front3(''))

"""
Other way it can be done

def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 
  
  # Could omit the if logic, and write simply front = str[:3]
  # since the slice is silent about out-of-bounds conditions.
"""