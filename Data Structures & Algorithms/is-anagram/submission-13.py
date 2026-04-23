class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if both strings are anagrams
        #return False if they aren't anagrams

        #first check if both lengths are equal
        #if len s != lenT then its false
        if len(s) != len(t):
            return False

        #we need to store the count of both of these 
        storageS = {}
        storageT = {}

        #iterate through string s
        for letter in s:
            #if letter is in storageS then add 1 to the count
            if letter in storageS:
                storageS[letter] += 1
            #else add it to the storage with count 1
            else:
                storageS[letter] = 1

        #iterate through string t
        for letter in t:
            #if letter is in storageT then add 1 to the count
            if letter in storageT:
                storageT[letter] += 1
            #else add it to the storage with count 1
            else:
                storageT[letter] = 1

        #make sure the count of both are equal
        if storageS != storageT:
            return False
        return True
        
        