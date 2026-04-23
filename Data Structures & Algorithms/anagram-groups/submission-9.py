class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all the similar character wrods together 
        #return the output in any order

        #store the character count and the amount of letters in a dictionary
        storage = {}

        #iterate through each words in all of strs 
        for words in strs:
            #then have a count to to map all of the letter places
            count = [0] * 26
            #iterate through all of letters in each of the words
            for letters in words:
                #to map each letter do the count ord letter - count ord a
                #then add one to that map
                count[ord(letters) - ord("a")] += 1
            #make the count into a tuple
            key = tuple(count)

            #check if key is in storage
            if key not in storage:
                #if its not in there make a new list for the key
                storage[key] = []
            #append the word that matches the key
            storage[key].append(words)
        #return it in a list form and only the values
        return list(storage.values())

