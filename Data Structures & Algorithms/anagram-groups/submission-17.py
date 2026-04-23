class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we need to store these anagrams into groups
        storage = {}

        #iterate trhough each word in the strs:
        for word in strs:
            #start a count and make sure theres one for each letter
            count = [0] * 26
            #now iterate through each letter in teh words
            for letter in word:
                #access count and do ord a - ord letter and add a + 1 to the position
                count[ord("a") - ord(letter)] += 1
            #So now make a tuple out of the positions 
            key = tuple(count)
            #so now check if this position is in storage
            if key not in storage:
                #if its not then create a new list for the key 
                storage[key] = []
            #append the word to this list 
            storage[key].append(word)
        #return the values of the storage in list form
        return list(storage.values())