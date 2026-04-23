class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #if length is not the same return false
        if len(s) != len(t):
            return False
        #return True if both strings are anagrams 
        #return False if they arent anagrams

        #create a storageS to hold s values
        storageS = {}
        #loop through s
        for letter in s:
            #if our value is in storageS
            if letter in storageS:
                #add 1 to the value
                storageS[letter] +=1 
            #else add value with 1
            else:
                storageS[letter] = 1
        print(storageS)
    
        #create a storageS to hold s values
        storageT = {}
        #loop through s
        for letter in t:
            #if our value is in storageS
            if letter in storageT:
                #add 1 to the value
                storageT[letter] +=1 
            #else add value with 1
            else:
                storageT[letter] = 1
        print(storageT)

        #compare both sotrage t and s
        if storageS != storageT:
            return False
        return True


        