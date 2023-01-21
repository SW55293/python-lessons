# -*- coding: utf-8 -*-
"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
We are in trouble if they are both smiling or if neither of them is smiling. 
Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""

def monkey_trouble(a_smile, b_smile):
  if (a_smile == True and b_smile == False) or (a_smile == False and b_smile == True):
    return False
  return True

print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
print(monkey_trouble(False, True))
