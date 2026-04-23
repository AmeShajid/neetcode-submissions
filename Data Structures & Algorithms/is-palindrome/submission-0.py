class Solution:
    def isPalindrome(self, s: str) -> bool:
        #make everything into the same case
        s = s.lower()

        #make a cleaned version of the string
        clean = ""
        #iterate through string
        for char in s:
            #only keep the letters and numbers
            if ("a" <= char <= "z") or ("0" <= char <= "9"):
                clean += char

        #now make two pointer
        #left is the first pointer start from beginning
        left = 0
        #j is the one that starts from the back
        right = len(clean) - 1

        #now start a while loop to make sure left is less than right thats so they dont cross
        while left < right:
            #if clean starting from the first != clean ending letter its false
            if clean[left] != clean[right]:
                return False
            #else just add +1 to left and -1 to right
            left += 1
            right -= 1
        return True
        