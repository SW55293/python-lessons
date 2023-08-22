from typing import List


# First solution
def wordBreak(s: str, wordDict: List[str]) -> bool:
    # Create a set for faster word lookup
    wordSet = set(wordDict)

    # Initialize a list to track whether substrings can be segmented
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Base case: an empty string can always be segmented

    for x in range(1, len(s) + 1):
        for y in range(x):
            # Check if the substring s[j:i] can be segmented
            if dp[y] and s[y:x] in wordSet:
                dp[x] = True
                break

    return dp[len(s)]
'''
We create a set wordSet for faster lookup of words from wordDict.

We initialize a dynamic programming list dp of size len(s) + 1. dp[i] will be True if the substring s[:i] can be segmented using words from wordDict.

We set dp[0] to True since an empty string can always be segmented.

We iterate over each position x in the string s.

For each position x, we iterate over all positions y before x. We check if the substring s[y:x] can be segmented and if s[y:x] is in wordSet. If both conditions are met and dp[y] is True, then we set dp[x] to True to indicate that the substring s[:x] can be segmented.

After completing the loops, we return dp[len(s)], which indicates whether the entire string s can be segmented using words from wordDict.

This approach properly checks all possible combinations of words from the wordDict to determine if the string s can be segmented as described in your task.
'''


# Second Solution
def wordBreak(s: str, wordDict: List[str]) -> bool:
       dp = [False] * (len(s) +1)
       dp[len(s)] = True
       for x in range(len(s)-1,-1,-1):
           for y in wordDict:
               if (x + len(y)) <= len(s) and s[x:x+len(y)] == y:
                   dp[x] = dp[x+len(y)]
               if dp[x]:
                   break
       return dp[0]