# Pattern          = Recursion
# Time Complexity  = O(n)
# Space Complexity = O(1)
"""
Input 1     = Tree Node
Return Type = Tree Node
"""

def isPalindrome(s):
   
    new_s = ""

    for x in s:
        if x.isalnum(): 
            new_s = new_s + x.lower()
    return new_s == new_s[::-1]