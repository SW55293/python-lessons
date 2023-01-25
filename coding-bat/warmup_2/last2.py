# -*- coding: utf-8 -*-
"""
Given a string, return the count of the number of times that a substring length 2 
appears in the string and also as the last 2 chars of the string, 
so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""
def last2(str):
  #short string 
  if len(str) <= 2:
    return 0
    
  #getting the last 2 characters
  lastTwo = str[len(str)-2:]
  count = 0
  
  #Going to check each pair of substring starting at 0 but not checking the last 2
  for s in range(len(str)-2):
    substring = str[s:s+2]
    if substring == lastTwo:
      count = count + 1
      
  return count
  
print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
print(last2('xxaxxaxxaxx'))
print(last2('xaxaxaxx'))
print(last2('xxxx'))
print(last2('13121312'))
print(last2('11212'))
print(last2('13121311'))
print(last2('1717171'))
print(last2('hi'))
print(last2('h'))
print(last2(''))