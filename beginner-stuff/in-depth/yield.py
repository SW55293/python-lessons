l1 = [num for num in range(1,20)]

#map function
my_map = map(lambda x: x**3, l1)
print(list(my_map))

#for the next function it should just print one by one
#what comes next but since we used the map and list 
#the iteeration is exhausted and we get a StopIteration
# print(next(my_map))

print('------Map Generator Clone---------')
l2 = [num for num in range(1,10)]
#Creating a Map clone that does the same as a map function
def map_clone(x, iterable_input):
    result = []
    for item in iterable_input:
        result.append(x(item))

    return result

print(l2)
cube_l2 = map_clone(lambda x: x**3, l2)
print(cube_l2)

print('------Creating New Generator ---------')
l3 = [num for num in range(1,10)]
def new_generator(x, itr_inp_2):
    for item in itr_inp_2:
        yield x(item)

print(l3)
square_l3 = new_generator(lambda x: x**2, l3)
print(square_l3)
#this down here will first print the first item in that list and
#then the next and so on until it gets to the list() casting print
#statement where it ends up printing the rest of the list
print(next(square_l3))
print(next(square_l3))
print(next(square_l3))
print(list(square_l3))