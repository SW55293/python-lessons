prizes = [5, 10, 15, 220, 1000]

#1st way doubles the prizes list with a for looop
double_prize = []
for x in prizes:
    double_prize.append(x * 2)

print(double_prize)

#2nd way that uses list comprehension
dbl_priz = [p * 2 for p in prizes]
print(dbl_priz)

#####################################################################
#3 square the even numbers
nums = [1,2,3,4,5,6]

square_evens = []
for n in nums:
    if(n ** 2) % 2 ==0:
        square_evens.append(n ** 2)
print(square_evens)

#4 Comprehension way
squared_evens_two = [n ** 2 for n in nums if (n ** 2) % 2 == 0]
print(squared_evens_two)