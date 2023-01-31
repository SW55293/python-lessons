# -*- coding: utf-8 -*-
''' 
Given 2 strings, return their concatenation, except omit the first char of each.
The strings will be at least length 1.


non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
''' 
def non_start(a, b):
  cut_a = a[1:]
  cut_b = b[1:]
  return cut_a + cut_b

print(non_start('Hello', 'There'))
print(non_start('java', 'code'))
print(non_start('shotl', 'java'))
print(non_start('ab', 'xy'))
print(non_start('ab', 'x'))
print(non_start('x', 'ac'))
print(non_start('a', 'x'))
print(non_start('kit', 'kat'))
print(non_start('mart', 'dart'))