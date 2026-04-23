class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #storage for sorted anagrams
        storage = {}
        #iterate the words in strs
        for word in strs:
            #start a count * 26 to map where the location is
            count = [0] * 26
            #iterate  the letters in word
            for letter in word:
                #tracking letters
                #to get count do ascii(letter) - ascii(a) to find position for mapping
                #add 1 to the position to map it
                count[ord(letter) - ord("a")] += 1

            #convert this into a tuple to store as a key in storage
            key = tuple(count)

            #check if its in storage
            if key not in storage:
                #create a new list
                storage[key] = []
                #append to that key the count
            storage[key].append(word)
        #return as a list and aonly get the values
        return list(storage.values())
        