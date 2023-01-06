# Split
str = "stephanie and me"
print(str.split(' '))

# Concat ints
l1 = [1,5,6,8,88]
l2 = [56,89,75,63,111,000]
print(l1 + l2)

#change value at certain index
l1[0] = -1
print(l1)

# append a value to a list
l2.append(1000000)
print(l2)

# removing the last value in a list with pop
print("before pop ", l1)
l1.pop()
print("after pop ", l1)

# removing certain elements in a list with remove
print("before removing 89 ", l2)
l2.remove(89)
print("after removing 89 ", l2)

# using del to delete a value at certain index
del(l2[2])
print(l2)

#adding different types of variables to a list
letters = ["a", "b", "c"]
letters.append(100)
print(letters)

#making a list within a list
nums = [letters, 90, 90, 90, l1, l2]
print(nums)
print("first list in nums ", nums[0])
print("get position of var within the list of nums ", nums[0][2])