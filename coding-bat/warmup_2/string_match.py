# -*- coding: utf-8 -*-
"""

Given 2 strings, a and b, return the number of the positions where they contain the 
same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" 
substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""
def string_match(a, b):
  count = 0
  for s in range(len(a)-1):
    if a[s:s+2] == b[s:s+2]:
      count += 1
  return count

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))
print(string_match('hello', 'he'))
print(string_match('he', 'hello'))	
print(string_match('h', 'hello'))	
print(string_match('', 'hello'))
print(string_match('aabbccdd', 'abbbxxd'))	
print(string_match('aaxxaaxx', 'iaxxai'))
print(string_match('iaxxai', 'aaxxaaxx'))