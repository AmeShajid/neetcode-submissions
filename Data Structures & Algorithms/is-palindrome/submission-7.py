class Solution:
    def isPalindrome(self, s: str) -> bool:
        #return true if palindrome return false if not palindrome
        
        #MAKE everything the same case
        s = s.lower()

        #create a string var 
        string = ""
        #iterate through str
        for letter in s:
            #if letter is between all letters or number 
            if ("a" <= letter <= "z") or ("0" <= letter <= "9"):
                #add it to string 
                string += letter

        #start a left pointer
        left = 0
        #start a rigth pointer 
        right = len(string) - 1

        #loops both pointers
        while left < right: 
            #if the string var left doesn't equal right 
            if string[left] != string[right]:
                #return False
                return False
            #else
            else:
                #left + 1
                left += 1
                #right - 1
                right -= 1
        #retunr true
        return True
        