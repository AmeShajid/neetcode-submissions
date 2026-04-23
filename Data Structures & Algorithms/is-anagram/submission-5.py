class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return False if the lengths are different
        if len(s) != len(t):
            return False
        
        #dictionary for string1
        string1 = {}

        #dictionary for string2
        string2 = {}

        #iteratre through the string
        for letter in s:
        #iteratre through the string
            if letter in string1:
                string1[letter] += 1
            #or else set it equal to 1
            else:
                string1[letter] = 1

        #iteratre through the string
        for letter in t:
            #iteratre through the string
            if letter in string2:
                string2[letter] += 1
            #or else set it equal to 1
            else:
                string2[letter] = 1

        # Compare both dictionaries
        if string1 != string2:
            return False
        else:
            return True

        