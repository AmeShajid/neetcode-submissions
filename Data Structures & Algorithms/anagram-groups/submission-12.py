class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all the anagrams togeher in their respective families

        #we need to store all of these words, and mapped letters 
        storage = {}

        #iterate through all of the words
        for words in strs:
            #start the mapping here for each letter create an entry
            count = [0] * 26
            #iterate through each letter in the words
            for letter in words:
                #access count 
                #get the ascii of the letter - ascii of a to map locatino 
                count[ord(letter) - ord("a")] += 1
            #once we make that then we make this into the key for the dictionary and make it into a tuple
            key = tuple(count)
            #if the key is not in our storage 
            if key not in storage:
                #create a new list for this key
                storage[key] = []
            #now we need to append the words to this locaiotn
            storage[key].append(words)
        #return the values but in a list
        return list(storage.values())        