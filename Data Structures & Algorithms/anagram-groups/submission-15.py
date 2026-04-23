class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all the anagrams together

        #we need to store the groups of letters that are the same
        storage = {}
        #we first need to iterate through strs
        for word in strs:
            #so now we need to start a count to map each one
            #26 because there are 26 letters
            count = [0] * 26
            #we need to iterate through letters in each owrd now
            for letter in word:
                #we need to replace the count values
                count[ord(letter) - ord("a")] += 1
            #so now we are going to create our key from the tuples
            key = tuple(count)
            #now check if this key is in storage
            if key not in storage:
                #if its not create a new list for it
                storage[key] = []
            #add the words to that list 
            storage[key].append(word)
        return list(storage.values())



        