# For loops can be used to iterated through list etc..
# For Loops = Iteration | Iterate

nums = [1,2,5,8,88,78]

# ways to get the sum
sum = 0
for n in nums:
    sum = sum + n  # sum += num
print(sum)

# using the range class. You need to also use the len() method
total = 0
for n in range(len(nums)):
    total = total + nums[n] # sum += num[n]
print(total)


# Usign the range() function
# to print the numbers from 10 numbers
print(list(range(0,10)))
print(list(range(1,11)))

#adding a stop gap(skips numbers)
print(list(range(0,10,2)))