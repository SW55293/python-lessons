# -*- coding: utf-8 -*-
"""
The parameter weekday is True if it is a weekday, and the parameter vacation is 
True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. 
Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""


def sleep_in(weekday, vacation):
  if weekday == vacation:
    return True
  elif weekday == False and vacation == True:
      return True
  return False


print(sleep_in(True, True))
print(sleep_in(False, True))
print(sleep_in(True, False))
print(sleep_in(False, False))


