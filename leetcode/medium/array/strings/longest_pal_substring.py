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
