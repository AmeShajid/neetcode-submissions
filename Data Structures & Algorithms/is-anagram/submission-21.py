class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #storage for both anagrams
        storage_s = {}
        storage_t = {}

        #iterate through s or t
        for letter in s:
            #if letter in s then add 1
            if letter in storage_s:
                storage_s[letter] += 1
            #else add it to the storage
            else:
                storage_s[letter] = 1
        
        #same for t
        for letter in t:
            if letter in storage_t:
                storage_t[letter] += 1
            else:
                storage_t[letter] = 1

        #check len of both 
        if storage_s != storage_t:
            return False
        return True 
        