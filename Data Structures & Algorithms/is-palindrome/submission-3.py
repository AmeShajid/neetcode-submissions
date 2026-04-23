class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first put everything in the same case
        s = s.lower()

        #then we need to make a clean string
        clean_string = ""

        #now iterate through every string
        for char in s:
            #now we only want letters and numbers
            if ("a" <= char <= "z") or ("0" <= char <= "9"):
                #add these characters too clean
                clean_string += char
        
        #now we need to set our pointers
        left = 0
        right = len(clean_string) - 1

        #now we start our loop 
        #make sure left doesn't cross over right
        while left < right:
            if clean_string[left] != clean_string[right]:
                return False
            #lse just add 1 from the left adn subtract 1 from the irght
            left += 1
            right -= 1
        return True


        
        