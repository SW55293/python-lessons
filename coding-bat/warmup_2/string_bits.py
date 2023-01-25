# -*- coding: utf-8 -*-
"""
Given a string, return a new string made of every other char
starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""
def string_bits(str):
  new_str = ''
  for s in range(len(str)):
    if s % 2 == 0:
      new_str = new_str + str[s]
  return new_str


print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
print(string_bits('HiHiHi'))
print(string_bits(''))
print(string_bits('Greetings'))	
print(string_bits('Chocoate'))
print(string_bits('pi'))
print(string_bits('Hello Kitten'))
print(string_bits('hxaxpxpxy'))

"""
When a problem wants you to skip every other one
think about modulos/remainder

Think of modulus as
example:
5 % 2  // 5 = x and 2 = y

x - (x/y) * y //here the division portion throws remainders out the window so dont worry about them ignore basically
so
5 - (5/2) * 2

5 - (2) * 2
5 - 4 = 1
answer=1
"""