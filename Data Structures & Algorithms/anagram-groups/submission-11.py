class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #store these values
        storage = {}

        #iterate through all of strs
        for words in strs:
            #start a count to map which letter is being accesed * 26 letters
            count = [0] * 26
            #iterate through all of the word
            for letters in words:
                #access count and do the ord(letter) - ord(a) add 1 to the location
                count[ord(letters) - ord("a")] += 1
            #then make that into a key tuple so we can put it in our storage
            key = tuple(count)

            #if that key is not in our storage
            if key not in storage:
                #create a new list for the key
                storage[key] = []
            #then append the words to that list
            storage[key].append(words)
        #return it as a list and only the storage values
        return list(storage.values())
        