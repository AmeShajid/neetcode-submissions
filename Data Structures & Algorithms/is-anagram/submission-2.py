class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if both strings are anagrams
        #return False if not

        #if chracters not same
        if len(s) != len(t):
            return False
        
        #make two dictionaries too store both strings
        CountS = {}
        CountT = {}

        #iterate through each letter in s
        for letter in s:

            if letter not in CountS:
                CountS[letter] = 1
            else:
                CountS[letter] += 1
        print(CountS)

        for letter in t:
            
            if letter not in CountT:
                CountT[letter] = 1

            else:
                CountT[letter] += 1
        print(CountT)

        if CountS == CountT:
            return True
        else:
            return False

        
        