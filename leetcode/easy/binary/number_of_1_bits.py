def count_1s(n):
    counter = 0

    # will run until it reaches the end of the int
    while n:
         #this will add 1 to the counter every time a 1 is moded by 2
        counter += n % 2
         #the bits are being looked at 1 by 1 so once we've looked at a number/bit 
         #then shift right to get rid of it and look at the next number
        n = n >> 1
    return counter

def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

print(count_1s(10))


  


'''
To quickly mod something
take the moder and list out its multiples
you want to either use the number that multiplies into it
or use the closest number under it

11 mod 2

multiples of 2 = 0,2,4,6,8,10..
So since 2 x 5 = 10 that is the closest we can get to 11 without going over
we subtract it from the pre-mod number and the answer is the remaider
11 - 10 = 1
'''

'''
Example
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.


we mod every single number in n the input. We know all 0 mod 2 will give us a zero. 
We also know that if we see a 1 and mod it by 2 we get 1 remainder

1 mod 2 
multiples of 2 = 0,2,4,6..
(we are going to use 2x0=0, because thats the closest we get to 1 wihtout going over)
so..

1 - 0 = 1
So our answer to 1 mod 2 = 1

every time we mod 2 a 1 we get 1 and add it to the counter. We then shift right to continue
down the input running the same formula
'''