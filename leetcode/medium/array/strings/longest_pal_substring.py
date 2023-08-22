#my code, it was too slow and got "Time Limit Exceeded"
def longestPalindrome(s: str) -> str:
    substrings = []
    for x in range(0, len(s)):
        for y in range(0, len(s) - x):
            substrings.append(s[y:x + y + 1])
    
    longest = ''
    for i in substrings:
        if i == i[::-1]:
            if len(i[::-1]) > len(longest): 
                longest =  i[::-1]
    return longest

#better code

def longestPalindrome(s: str) -> str:

    def expandAroundCenter(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
    longest = ""
    for x in range(len(s)):
        # Odd length palindrome
        odd = expandAroundCenter(x, x)
        # Even length palindrome
        even = expandAroundCenter(x, x + 1)
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    return longest



