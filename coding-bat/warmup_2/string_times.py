# -*- coding: utf-8 -*-
"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""
def string_times(str, n):
  return str * n



print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))
print(string_times('Hi', 0))
print(string_times('Hi', 5))
print(string_times('Oh Boy!', 2))
print(string_times('x', 4))
print(string_times('', 4))
print(string_times('code', 2))
print(string_times('code', 3))


"""
Other way it can be done

def string_times(str, n):
  result = ""
  # range(n) is [0, 1, 2, .... n-1]
  for i in range(n):  
    result = result + str /// or result += str
  return result
"""