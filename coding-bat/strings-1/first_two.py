# -*- coding: utf-8 -*-
"""

Given a string, return the string made of its first two chars, so the String
"Hello" yields "He". If the string is shorter than length 2, return whatever 
there is, so "X" yields "X", and the empty string "" yields the empty string "".


first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
"""
def first_two(str):
  if len(str) < 2:
    return str
  
  first2 = str[:2]
  return first2

# Another way to do it
# def first_two(str):
#   if len(str) >= 2:
#     return str[:2]
#   else:
#     return str

print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))
print(first_two('a'))
print(first_two(''))
print(first_two('Kitten'))
print(first_two('hi'))
print(first_two('hiya'))