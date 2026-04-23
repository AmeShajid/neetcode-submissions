class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first make this lowe case
        s = s.lower()
        #first we need to make this into one string
        full_string = ""
        #iterate through s and add each letter
        for letter in s:
            #now we need to make sure its only letter nad numbers we are adding
            if ("a" <= letter <= "z") or ("0" <= letter <= "9"):
                #tyhen add it to string
                full_string += letter
        print(full_string)

        #now we need to set our pointers
        left = 0
        right = len(full_string) - 1
        
        #now we need to iterate through the string until both meet
        while left < right:
            #so now if fuyll string left value doesnt equal right value its false
            if full_string[left] != full_string[right]:
                return False
            #else add 1 to left and -1 to right
            else:
                left += 1
                right -= 1
        return True