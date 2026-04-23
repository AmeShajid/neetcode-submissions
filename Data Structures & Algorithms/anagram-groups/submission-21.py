class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #storage for words
        storage = {}

        #iterate through each word
        for word in strs:
            #start a count for each letter
            count = [0] * 26
            #iterate th rough each letter in word
            for letter in word:
                #add 1 to count to map it
                count[ord(letter) - ord("a")] += 1
            #create a key tuple out of this
            key = tuple(count)
            #if teh key not in storage
            if key not in storage:
                #create an emmpty list to append to 
                storage[key] = []
            #append to storage using key 
            storage[key].append(word)
        #return list of values 
        return list(storage.values())

        
        