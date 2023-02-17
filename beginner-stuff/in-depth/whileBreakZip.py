from random import randint
# while loops, break and pass, generator, zip function

#while loops keep running if something is True
truth_cond = True
while truth_cond:
    print('this will keep running until it hits a break')
    break

# small program to look for athe number 25 in a random list
list_of_random = [randint(1, 100) for num in range(1000)]
lucky_num = 25
n = 0
while n < len(list_of_random):
    if list_of_random[n] == lucky_num:
        print(f'lucky number found at index = {n}')
        # break. you can add a break here to stop when you find the first 25 
    n += 1

# we can use the enumerate function that gives us the index associated with an item
print('------------------------')
for index, num in enumerate(list_of_random):
    if num == lucky_num:
        print(f'{lucky_num} found at {index}')
        break

# Zip function
#takes 2 lists and pairs them 
#output would be l1+l2[0,0] l1+l2[1,1] etc...
l1 = ['.py', '.java', '.rb,', '.js', '.c']
l2 = ['python', 'javascript', 'ruby', 'java', 'c']

tuple_list = list(zip(l2,l1))
print(tuple_list)