class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #create two storages to keep track of both counts 
        storageS = {}
        storageT = {}

        #iterate through strings
        for letter in s:
            #if letter is in storage  
            if letter in storageS:  
                #add a + 1 to the letter value
                storageS[letter] += 1
            #else 
            else:
                #add a 1 to the value for the letter
                storageS[letter] = 1
        print(storageS)

        #iterate through strings
        for letter in t:
            #if letter is in storage  
            if letter in storageT:  
                #add a + 1 to the letter value
                storageT[letter] += 1
            #else 
            else:
                #add a 1 to the value for the letter
                storageT[letter] = 1
        print(storageT)

        #now check to see if both dicts are same
        if storageS != storageT:
            return False
        return True
            
        
        
        