class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if both strings are equal
        #return False if strings are NOT equal

        #create two storages
        storage_s = {}
        storage_t = {}
        
        #iterate through string
        for letter in s:
            #if string is inside of storage
            if letter in storage_s:
                #add 1 to count
                storage_s[letter] += 1
            #else 
            else:
                #add it to storage
                storage_s[letter] = 1

        #iterate through string
        for letter in t:
            #if string is inside of storage
            if letter in storage_t:
                #add 1 to count
                storage_t[letter] += 1
            #else 
            else:
                #add it to storage
                storage_t[letter] = 1

        #check if len of both is equal 
        if storage_t != storage_s:
            return False
        return True
        
        