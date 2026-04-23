class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if both strings are anagrams
        #return False if both strings aren't anagrams


        #make sure they are both equal 
        if len(s) != len(t):
            return False
        #Store string s letters
        storage_s = {}

        #store string t letters
        storage_t = {}

        #iteate through string s
        for letter in s:
            #if the letter is in storage s 
            if letter in storage_s:
                #add 1 to that count
                storage_s[letter] += 1
            #else
            else:
                #add that letter to the storage
                storage_s[letter] = 1

        #iteate through string t
        for letter in t:
            #if the letter is in storage t
            if letter in storage_t:
                #add 1 to that count
                storage_t[letter] += 1
            #else
            else:
                #add that letter to the storage
                storage_t[letter] = 1

        if storage_s != storage_t:
            return False
        return True 
        