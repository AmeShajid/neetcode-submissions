class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #return True if both strings are anagrams
        #return False if not true

        #first case if they are not same length its false
        if len(s) != len(t):
            return False

        #store letters of s
        storageS = {}
        #store letters of t
        storageT = {}

        #iterate through s string
        for letter in s:
            #if letter is in storages 
            if letter in storageS:
                #add 1 to value
                storageS[letter] += 1
            #else add it to the storageS
            else:
                storageS[letter] = 1

        #iterate through t string
        for letter in t:
            #if letter is in storaget 
            if letter in storageT:
                #add 1 to value
                storageT[letter] += 1
            #else add it to the storaget
            else:
                storageT[letter] = 1

        if storageS != storageT:
            return False
        else:
            return True

        