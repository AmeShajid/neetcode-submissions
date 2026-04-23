class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #return the anagrams grouped together 

        #first we need to create a storage
        storage = {}
        
        #iterate through strs
        for word in strs:
            #create a count for every letter
            count = [0] * 26
            #iterate through every letter in the word
            for letter in word:
                #update count with an update position of 1 using ord subtraction 
                count[ord("a") - ord(letter)] += 1
            #create a key by making every matching one into a tuple
            key = tuple(count)
            #if the key is not in our storage
            if key not in storage:
                #create an empty list for the dictionary
                storage[key] = []
            #append those words to this empty position 
            storage[key].append(word)
        #return the values
        return list(storage.values())


        
        