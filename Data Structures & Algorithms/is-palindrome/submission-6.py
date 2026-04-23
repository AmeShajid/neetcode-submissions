class Solution:
    def isPalindrome(self, s: str) -> bool:
        #so first we want everything in teh same case
        s = s.lower()

        #then we need to make sure we only have letters and numbers in the string
        full_string = ""
        for letter in s:
            if ("a" <= letter <= "z") or ("0" <= letter <= "9"):
                full_string += letter
        print(full_string)

        #start a two pointer
        #left 
        left = 0
        #right
        right = len(full_string) -1
        #while loop until we are done length of string
        while left < right:
            #if left and right dont matvh
            if full_string[left] != full_string[right]:
                #return False
                return False
            #else
            else:
                #move the left + 1 
                left += 1
                #and right -1
                right -= 1
        #return true
        return True
            

        
        