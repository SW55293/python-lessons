# -*- coding: utf-8 -*-
"""
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag 
and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
"""
def make_tags(tag, word):
  open_tag = '<' + tag + '>'
  close_tag = '</' + tag + '>'
  
  return open_tag + word + close_tag

print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))	
print(make_tags('cite', 'Yay'))
print(make_tags('address', 'here'))
print(make_tags('body', 'Heart'))
print(make_tags('i', 'i'))
print(make_tags('i', ''))