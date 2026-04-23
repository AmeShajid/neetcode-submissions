class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #storage for all the numbers
        storage = {}

        #iterate through strs
        for words in strs:
            #create a count for 26 spots
            count = [0] * 26
            #iterate through letters in word
            for letter in words:
                #count ord a - ord letter += 1
                count[ord("a") - ord(letter)] += 1
            #create a key for the tuple
            key = tuple(count)
            #if the key not in dict
            if key not in storage:
                #create a empty list for that key
                storage[key] = []
            #append the word to the list
            storage[key].append(words)
        #return as a list the values
        return list(storage.values())
        
        