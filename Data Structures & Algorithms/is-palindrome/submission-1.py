class Solution:
    def isPalindrome(self, s: str) -> bool:
        #return true if it is a palindrome
        #return False if it is not a palindrome

        #first we need to make everythign in same case
        s = s.lower()

        #first we need to clean this string
        clean_string = ""

        #now iterate through every chracter in string
        for char in s:
            #we only want letters and numbers
            if ("a" <= char <= "z") or ("0" <= char <= "9"):
                #add these chracters too clean
                clean_string += char
                    
        #now we need to set our two pointers
        #one at the beginning
        left = 0
        #one at the end
        right = len(clean_string) - 1

        #Now start our loop
        #make sure left and right dont cross
        while left < right:
            #if our left != our right then its false
            if clean_string[left] != clean_string[right]:
                return False
            #else just add 1 from the left and -1 from the right to continue
            left += 1
            right -=1
        return True
