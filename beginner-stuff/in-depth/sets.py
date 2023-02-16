# Sets are unordered collection of elements
# they dont have indices 
# they cannot contain duplicates/will not show there are duplicates
# every time you print it, it will give you a different order

set1 = {23, 5,5,6325, 6.09, 'names', 'dog', 'bark', 'bark', 23, 'java'}
print(set1)

# you can remove duplicates using casting
my_new_set = []
set1 = set(my_new_set)
# if you check the print statement the string 'bark and 23 were removed

#reasons to use sets are because searching and doing math operations is optimized
#the time complexity is fast

#finding/serching using in
print('steph' in set1)

set2 = {23, 5,5,6325, 6.09, 'names', 'dog', 'bark', 'bark', 23, 'java'}
#testing math operation methods
programming = {'java', 'python', 'c#', 'c++', 'javascript', 23}

#intersection looks for anything the 2 sets have in common and prints it
print(set2.intersection(programming))

#put both of the sets together with union
print(set2.union(programming))

#prints out all the elements that are not found in programming
print(set2.difference(programming))
#prints out all the elements that are not found in set2
print(programming.difference(set2))