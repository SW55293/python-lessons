def characterReplacement(s, k):
        """
        :input type s: str
        :input type k: int
        :return type: int
        """
        dict = {} #keep track of all characters and their frequencies
        left = 0
        max_char_freq = 0 #will keep track of the char count with most occurences
        longest_sub = 0
        
        #This loop iterates over the characters in the string, from left to right.
        for right in range(len(s)):
            #This line increments the count of the character at right in the dictionary. 
            #If the character does not already exist in the dictionary, then it is added with a count of 1.
            #calling this dict[s[right]] gives us the index position within the dictionary
            #where that letter is at. s[right] by itself shows a character but inside of the dict[]
            #we get a number because it's the index position of that char
            dict[s[right]] = 1 + dict.get(s[right], 0)
            #This line updates the maximum frequency of any character to the maximum 
            #of the current maximum frequency and the count of the character at right.
            max_char_freq = max(max_char_freq, dict[s[right]])
            print(dict.get(s[right])) #gets the value at that position
            #This condition checks if the substring from left to right has more than
            # k characters that appear more than once.
            if (right - left + 1) - max_char_freq > k:

                #If the condition is true, then we need to remove one of the characters 
                #from the substring. This is done by decrementing the count of the character 
                #at left and then incrementing left to move the window one character to the right.
                dict[s[left]] -= 1
                left += 1

            #This line updates the length of the longest substring to the maximum of the current 
            #length and the length of the substring from left to right.
            longest_sub = max(longest_sub, right - left + 1)
        return longest_sub

print("answer = ", characterReplacement("ABAB", 2))