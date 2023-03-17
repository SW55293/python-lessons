# Pattern          = Dynamic Programming Bottom Up Approach
# Time Complexity  = O(n)
# Space Complexity = O(1)
"""
Input1 = 1 Integer
Return type = 1 Integer
"""



def climbingStairs(n):
    if n <= 3:
        return n
    n2 = 2
    n3 = 3

    for _ in range(n-3):
        print('n =', n)
        print('n-3 =', n-3)
        temp = n3
        print('temp =', temp)
        n3 = n2 + n3
        print('n3 =', n3)
        n2 = temp
        print('n2 =', n2)
    return n3







'''
I want to make my base at 3 because all numbers before 4 are just n.
With the if statement we took care of any n input thats less than 4
and now we set 2 variables equal to what n at input 2 & 3 would output.
We need these because we calculate the next number by adding the previous numbers


indices     1 2 3 4 5 
           --------------
           | 1 2 3 4 5
           -------------- 
n = 1 output = 1
n = 2 output = 2
n = 3 output = 3 <-- base (that why we iterate at position n-3 to account for our base)
n = 4 output = n=2 + n=3 = 2+3 = 5
n = 5 output = n=3 + n=4 = 3+5 = 8
'''

# Another Version
def climbStairs(n):
        """
        :Input type n: int
        :rtype: int
        """
        if n < 3:
            return n

        n1 = 1
        n2 = 1
        for _ in range(n-1):
            temp = n1
            n1 = n1 + n2
            n2 = temp
        return n1



print(climbingStairs(5))
# print(climbStairs(5))