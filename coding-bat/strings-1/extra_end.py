# -*- coding: utf-8 -*-
"""

Given a string, return a new string made of 3 copies of the last 2 chars
of the original string. The string length will be at least 2.


extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""
def extra_end(str):
  last2 = str[len(str)-2:]
  return last2 * 3

# Another solution
# def extra_end(str):
#   end = str[-2:]
#   return end + end + end

print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))	
print(extra_end('Candy'))
print(extra_end('Code'))


def practice(str):
    first2 = str[:2]
    last = str[len(str)-2]
    middle = len(str) // 2
    print(first2)
    print(str[middle:])
    print(last)
    return first2
print(practice('thanksgiving'))

"""
Getting the middle character of the string

middle = len(str) // 2
then you can either get the first half or last half

firs_half = str[:middle]
last_half = str[middle:]
"""