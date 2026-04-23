class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if both strings are equal 
        #return False if both strings are not equal 

        #storage for both strings
        storageS = {}
        storageT = {}
        #iterate through both strings 
        for letter in s:
            #if the letter is in storage
            if letter in storageS:
                #add 1 to the count
                storageS[letter] += 1
            #else
            else:
                #add it with 1 
                storageS[letter] = 1
        
        for letter in t:
            if letter in storageT:
                storageT[letter] += 1
            else:
                storageT[letter] = 1
        
        if storageS != storageT:
            return False
        return True
        

        