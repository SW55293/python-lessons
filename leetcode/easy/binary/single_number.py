
def singleNumber( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    single_num = 0

    for number in nums:
        print('number = ', number)
        print('single number before =', single_num)
        print('XOR =' , single_num ^ number)
       
        single_num = single_num ^ number
       
        print('single number after =', single_num)
        print('\n')

    return single_num




print('answers = ', singleNumber([2,2,1,8,9,9]))



'''
it turns the numbers into their bit significance
                           8421
0 ^ 2 = 2 -> 0000 ^ 0010 = 0010
2 ^ 2 = 0 -> 0010 ^ 0010 = 0000
0 ^ 1 = 1 -> 0000 ^ 0001 = 0001

'''