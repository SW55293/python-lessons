# -*- coding: utf-8 -*-
"""
Given two strings, a and b, return the result of putting them together in the 
order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".


make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
"""
def make_abba(a, b):
  return a + b + b + a


print(make_abba('Hi', 'Bye'))
print(make_abba('Yo', 'Alice'))
print(make_abba('What', 'Up'))
print(make_abba('aaa', 'bbb'))
print(make_abba('x', 'y'))
print(make_abba('x', ''))
print(make_abba('', 'y'))
print(make_abba('Bo', 'Ya'))
print(make_abba('Ya', 'Ya'))