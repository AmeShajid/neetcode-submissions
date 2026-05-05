class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #first start from last index
        i = len(s) - 1
        #get the length counter
        length = 0

        #iterate left while there is spaces
        while s[i] == " ":
            #go backwards
            i -= 1

        #ITERATE while we are in the word AND theres no space
        while i >= 0 and s[i] != " ":
            #go backwards
            length += 1
            #add to length
            i -= 1
        
        #return length 
        return length

        