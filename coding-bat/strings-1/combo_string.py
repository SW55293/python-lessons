# -*- coding: utf-8 -*-
''' 
Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).

combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'
''' 
def combo_string(a, b):
  if len(a) < len(b):
    return a + b + a
  return b + a + b


print(combo_string('Hello', 'hi'))
print(combo_string('hi', 'Hello'))
print(combo_string('aaa', 'b'))
print(combo_string('b', 'aaa'))
print(combo_string('aaa', ''))
print(combo_string('', 'bb'))
print(combo_string('aaa', '1234'))	
print(combo_string('aaa', 'bb'))
print(combo_string('a', 'bb'))
print(combo_string('bb', 'a'))
print(combo_string('xyz', 'ab'))