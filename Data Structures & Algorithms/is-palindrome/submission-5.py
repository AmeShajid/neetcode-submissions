class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first we need to lower this string
        s= s.lower()

        #then we need to store this string
        full_string = ""

        #now we need to iterate through this string
        for letter in s:
            #now we need to make sure that its only letters and numbers
            if ("a" <= letter <= "z") or ("0"<= letter <= "9"):
                #add a letter to teh string
                full_string += letter
        print(full_string)

        #now we need to check and make sure everything is equal 
        #set two pointers first
        left = 0
        right = len(full_string) - 1

        #now loop
        while left < right:
            #first check if the letters are equal
            if full_string[left] != full_string[right]:
                return False
            #so now if they are equal contineu moving the pointers
            else:
                left += 1
                right -= 1
        return True
        