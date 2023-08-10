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

'''
def isPalindrome(s):
    # This function takes a string as input and returns True if the string is a palindrome, False otherwise.

    # Initialize a new string to store the lowercase and alphanumeric characters of the input string.
    # The `isalnum()` method checks if a character is alphanumeric.
    # The `lower()` method converts a string to lowercase.
    new_s = ""

    # Iterate over the input string.
    for x in s:
        # If the character is alphanumeric,
        if x.isalnum():
            # Add the lowercase version of the character to the new string.
            new_s = new_s + x.lower()

    # Return True if the new string is equal to its reverse, False otherwise.
    # The `::-1` syntax reverses the string.
    return new_s == new_s[::-1]

'''