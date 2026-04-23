class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #we need to store these numbers 
        storage = {}

        #iterate through everything in strs
        for words in strs:
            #now we have to map each of the letters so its assigned to a letter
            #make a list * 26 because of 26 letter sin the alphabet
            count = [0] * 26
            #iterate through everything in words
            for letters in words:
                #to map each letter 
                #access count and then do ord(letters) - ord(a) +=1
                count[ord(letters) - ord("a")] += 1
            
            #once we have that convert that into a tuple
            key = tuple(count)

            #now check if that key is in our storage
            if key not in storage:
                #create a new list for that storage key
                storage[key] = []
            #then append the words for the location
            storage[key].append(words)

        #return the values as a list
        return list(storage.values())
        
        