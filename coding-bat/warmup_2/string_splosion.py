# -*- coding: utf-8 -*-
"""

Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""

def string_splosion(str):
  new_string = ''
  for s in range(len(str)):
    new_string = new_string + str[:s+1]
    print(new_string)
  return new_string
  

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
print(string_splosion('x'))
print(string_splosion('fade'))
print(string_splosion('There'))
print(string_splosion('Kitten'))
print(string_splosion('Bye'))
print(string_splosion('Good'))
print(string_splosion('Bad'))
# bad 
#when s=0 we get str[0:1] = b,   new_string = b
#when s=1 we get str[0:2] = ba,  new_string = b + ba 
#when s=2 we get str[0:3] = bad, new_string = b + ba + bad 
# = bbabad
""" 
On each iteration, add the substring of the characters 0..s
  
string_splosion('Code') →   'CCoCodCode' 


C
CCo
CCoCod
CCoCodCode
CCoCodCode

string_splosion('abc') →    'aababc'                   
string_splosion('ab') →     'aab'
string_splosion('x') →      'x'
string_splosion('fade') →   'ffafadfade'
string_splosion('There') →  'TThTheTherThere'
string_splosion('Kitten') → 'KKiKitKittKitteKitten'
string_splosion('Bye') →    'BByBye'
string_splosion('Good') →   'GGoGooGood'
string_splosion('Bad') →    'B Ba Bad'
  

a
aab
aababc
aababc
a
aab
aab
x
x
f
ffa
ffafad
ffafadfade
ffafadfade
T
TTh
TThThe
TThTheTher
TThTheTherThere
TThTheTherThere
K
KKi
KKiKit
KKiKitKitt
KKiKitKittKitte
KKiKitKittKitteKitten
KKiKitKittKitteKitten
B
BBy
BByBye
BByBye
G
GGo
GGoGoo
GGoGooGood
GGoGooGood
B
BBa
BBaBad
BBaBad
"""

  
