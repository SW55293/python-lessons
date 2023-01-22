# -*- coding: utf-8 -*-
"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""
def front_back(str):
  if len(str) <= 1:
    return str
  
  first = str[0]
  middle = str[1:len(str)-1]
  last = str[len(str)-1]

  return  last + middle + first

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))	
print(front_back('abc'))
print(front_back(''))
print(front_back('Chocolate'))
print(front_back('aavJ'))
print(front_back('hello'))