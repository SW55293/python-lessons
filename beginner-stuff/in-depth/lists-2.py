# Inserting Methods for a List
# append() | insert() | extend()

'''
append() - adds an item to the end of the list
insert() - adds item at  or between any index given
extend() - adds a list into an existing list but doesnt add the structure (basically appends)
'''
numbers = [1,3,6,9,4,5]
states = ['CA', 'NV', 'AZ']

#this will insert 0 at position 0
numbers.insert(0, 0)
print(numbers)

extra_list = ['NY', 'TX', 'FL']
#this will append the extra_list into the states list. At the end
states.extend(extra_list)
print(states)

##############################################################################
# Removing Methods from a list
# pop() | remove()
'''
pop()    - removes the last item in a list 
remove() - removes a specific item from a list
'''
#this removes CA from our list 
states.remove('CA')
print(states)

#this will remove the list item in our numbers list
#if you put pop() inside of print statement it tells you what its going to delete
print(numbers.pop())
print(numbers)

##############################################################################
# Slicing and Sublists
# [start : stop(not included)]
score = [12,20,45,4,78,10,1,3,6,6]

#prints the whole list
print(score[::])

#skips every other item
print(score[::2])

#print the list reversed
print(score[::-1])
#or use reverse() method
score.reverse()
print(score)