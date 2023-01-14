# map(function, data)
#maps can convert one type of list into another or just
#a list into another
from random import shuffle

def mix_it(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)



#form an anagram using a map
words = ['salad', 'milk', 'soda', 'ham']
anagrams = []

#1st way using a for loop and not the map function/method
for w in words:
    anagrams.append(mix_it(w))

print(anagrams)

#2nd way
print(list(map(mix_it, words)))

#3rd way
print([mix_it(w) for w in words])