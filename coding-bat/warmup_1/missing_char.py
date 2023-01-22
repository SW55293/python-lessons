# -*- coding: utf-8 -*-
"""
Given a non-empty string and an int n, return a new string where the char 
at index n has been removed. The value of n will be a valid index of a char 
in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""
def missing_char(str, n):
  new_str = ''
  for s in range(0, len(str)):
    if s != n:
      new_str = new_str + str[s]
  return new_str
      
    
#Second option   
# before = str[:n]
# after = str[n+1:]
# return before + after

# In this method, we have to run a loop and append the 
# characters and build a new string from the existing 
# characters except when the index is n. 
# (where n is the index of the character to be removed)

print(missing_char('kitten', 1))	
print(missing_char('kitten', 0))	
print(missing_char('kitten', 4))	
print(missing_char('Hi', 0))
print(missing_char('Hi', 1))
print(missing_char('code', 0))	
print(missing_char('code', 1))	
print(missing_char('code', 2))	
print(missing_char('code', 3))	
print(missing_char('chocolate', 8))