class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #we will need to store the mapping and words
        storage = {}

        #iterate through strs
        for word in strs:
            #create the mapping so we can count the letter for each word
            count = [0] * 26
            #iterate through each letter in the word from the strs
            for letter in word:
                #now to add the count we have to do ord letter - ord a += 1
                count[ord(letter) - ord("a")] += 1
            #once the mapping is created create it into a tuple for each word
            key = tuple(count)
            #check to see if this key is in storage
            if key not in storage:
                #if it is not then create an empty list
                storage[key] = []
            #if it exists then access key and append the words
            storage[key].append(word)
        #return in list form all the values from storage
        return list(storage.values())

        