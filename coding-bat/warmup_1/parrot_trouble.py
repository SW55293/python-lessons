# -*- coding: utf-8 -*-
"""
We have a loud talking parrot. The "hour" parameter is the 
current hour time in the range 0..23. We are in trouble if 
the parrot is talking and the hour is before 7 or after 20. 
Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False	
parrot_trouble(True, 21) → True
parrot_trouble(False, 21) → False
parrot_trouble(False, 20) → False
parrot_trouble(True, 23) → True	
parrot_trouble(False, 23) → False
parrot_trouble(True, 20) → False
parrot_trouble(False, 12) → False
"""

def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  return False
  
#return (talking and ( hour < 7 or hour > 20))

print(parrot_trouble(True, 6))	
print(parrot_trouble(True, 7))	
print(parrot_trouble(False, 6))
print(parrot_trouble(True, 21))
print(parrot_trouble(False, 21))
print(parrot_trouble(False, 20))
print(parrot_trouble(True, 23))
print(parrot_trouble(False, 23))	
print(parrot_trouble(True, 20))	
print(parrot_trouble(False, 12))