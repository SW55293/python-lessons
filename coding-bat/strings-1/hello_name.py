# -*- coding: utf-8 -*-
"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""
def hello_name(name):
  return 'Hello ' + name + '!'


print(hello_name('Bob'))
print(hello_name('Alice'))
print(hello_name('X'))
print(hello_name('Dolly'))
print(hello_name('Alpha'))
print(hello_name('Omega'))
print(hello_name('Goodbye'))
print(hello_name('ho ho ho'))
print(hello_name('xyz!'))	
print(hello_name('Hello'))