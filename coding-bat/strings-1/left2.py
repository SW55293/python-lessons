# -*- coding: utf-8 -*-
"""
Given a string, return a "rotated left 2" version where the first 2 
chars are moved to the end. The string length will be at least 2.


left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
"""
def left2(str):
  first_two = str[:2]
  new_str = ''
  
  for s in range(len(str)):
    if s > 1:
      new_str = new_str + str[s] 
  return new_str + first_two
    
# Another easier solution
# def left2(str):
#   return str[2:] + str[:2]

print(left2('Hello'))
print(left2('java')) 
print(left2('code'))
print(left2('cat'))
print(left2('12345'))
print(left2('Chocolate'))
print(left2('bricks'))