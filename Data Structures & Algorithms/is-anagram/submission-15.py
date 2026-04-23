class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if both strings are anagrams of each other
        #return False if both strings are not anagrams of each other
        

        #first we need to store both of these string chracters
        StorageS = {}
        StorageT = {}

        #now iterate through one of the strings
        for letter in s:
            #if the letter is in the storage
            if letter in StorageS:
                #plus one to the letter value
                StorageS[letter] += 1
            #else it means it isnt in the storage
            else:
                #add the letter with a value of 1
                StorageS[letter] = 1
        
        #now iterate through one of the strings
        for letter in t:
            #if the letter is in the storage
            if letter in StorageT:
                #plus one to the letter value
                StorageT[letter] += 1
            #else it means it isnt in the storage
            else:
                #add the letter with a value of 1
                StorageT[letter] = 1

        #now check if both of these are equal
        if StorageS != StorageT:
            return False
        return True
        
                
        

        