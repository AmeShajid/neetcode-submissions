class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #we need a storage to align all mapped counts with the words
        storage ={}

        #iterate through each word in strs
        for word in strs:
            #create a count of 26 0s
            count = [0] * 26
            #iterate through each letter in word
            for letter in word:
                #so now we need to acces the count and do ord a - ord letter += 1 to map it
                count[ord("a") - ord(letter)] += 1 
            #create a key tuple from that count 
            key = tuple(count)
            #check if this key is in our storage
            if key not in storage:
                #if it isnt then create an empty list in the values
                storage[key] = []
            #now we need to append the word to the empty list 
            storage[key].append(word)
        #return the list of values from the storage
        return list(storage.values())
        