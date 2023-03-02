#

l1 = [num for num in range(1,20)]
l2 = [num for num in range(1,20)]

#zip function
my_zip_gen = zip(l1,l2)
print(my_zip_gen)
print(list(my_zip_gen))

#map function
my_map = map(lambda x: x**3, l1)
print(my_map)
print(list(my_map))
#using for loop
for item in my_map:
    print(item)

#generators use up less space and are more efficient
#than for loops or iterators