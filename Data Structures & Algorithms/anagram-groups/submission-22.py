class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #storage to store letters / words
        storage = {}

        #first iterate through strings 
        for word in strs:
            #create the mapping 
            count = [0] * 26
            #now iterate through each letter
            for letter in word:
                #add a map to each count
                count[ord(letter) - ord("a")] += 1
            #once a map is made make it into a key and make each count into a touble 
            key = tuple(count)
            #if the key is not in the storage then create an empty list associated 
            if key not in storage:
                #create list 
                storage[key] = []
            #append to it 
            storage[key].append(word)
        #return all the vals as a list
        return list(storage.values())
        