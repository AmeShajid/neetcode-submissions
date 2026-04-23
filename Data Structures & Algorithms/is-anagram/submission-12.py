class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True = both strings are equal 
        #return False = both strings not equal 

        #first check if the lengths are equal
        if len(s) != len(t): 
            return False
        
        #store the letters in s
        StorageS = {}
        #iterate through s
        for letter in s:
            #check if the letter in StorageS
            if letter in StorageS:
                #add 1 to the count for that letter
                StorageS[letter] += 1
            #else start the count with 1
            else:
                StorageS[letter] = 1

        #store the letters in t
        StorageT = {}
        #iterate through s
        for letter in t:
            #check if the letter in StorageS
            if letter in StorageT:
                #add 1 to the count for that letter
                StorageT[letter] += 1
            #else start the count with 1
            else:
                StorageT[letter] = 1  

        #now make sure the dictionaries are equal 
        if StorageS == StorageT:
            return True
        return False
        