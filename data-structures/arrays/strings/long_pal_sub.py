# Two pointers start at the same position for odd and even gets 1 pointer at 1 point ahead. 
# we then move the pointers opposite directions and compare if the are the same char

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        def find_longest(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
# returning a range between s
        for x in range(len(s)):
            # odd length
            odd = find_longest(x,x)

            # even length
            even = find_longest(x,x+1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest



sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))




'''
My attempt, which did not pass all test cases

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s = ''.join(filter(str.isalnum, s))
        # s = s.lower()
        s = [new_s.lower() for new_s in s if new_s.isalnum()]
        left = 0
        right = len(s) - 1
        first_half = []
        second_half = []

        for _ in range(len(s)):
            if s[left] == s[right]:
                first_half.append(s[left])
                second_half.append(s[right])
                left += 1
                right -= 1
            if left == right and s[left] == s[right]:
                first_half.append(s[left])
            else:
                right -= 1
        left += 1
        first = ''.join([str(elem) for elem in first_half])
        second = ''.join([str(elem) for elem in second_half])

        return first + second[::-1]

'''