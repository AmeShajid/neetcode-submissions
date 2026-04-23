class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if both strings are equal
        #return False if strings are not equal

        #first lenghts have to be the same
        if len(s) != len(t):
            return False

        #we need to store the letters in a storage for both s and t
        storageS = {}
        storageT = {}

        #iterate through s string
        for letter in s:
            #if our letter is in storage then add another count
            if letter in storageS:
                storageS[letter] += 1
            else:
                storageS[letter] = 1
        print(storageS)

        #iterate through s string
        for letter in t:
            #if our letter is in storage then add another count
            if letter in storageT:
                storageT[letter] += 1
            else:
                storageT[letter] = 1
        print(storageT)

        if storageS == storageT:
            return True
        return False

        
        