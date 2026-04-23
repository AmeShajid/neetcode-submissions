class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if 2 strings == other
        #return False if both strings != other

        #storage for s string
        storageS = {}
        #stroage for t string
        storageT = {}

        #iterate through s string
        for letter in s:
            #if letter in stroage s:
            if letter in storageS:
                #update the position with 1
                storageS[letter] += 1 
            #else make the position == 1
            else:
                storageS[letter] = 1
        print(storageS)
       
        #iterate through t string
        for letter in t:
            #if letter in stroage t:
            if letter in storageT:
                #update the position with 1
                storageT[letter] += 1
            #else make the position == 1
            else:
                storageT[letter] = 1
        print(storageT)

        if storageS != storageT:
            return False
        return True

        

