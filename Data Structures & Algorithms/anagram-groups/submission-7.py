class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we need to store these numbers
        storage = {}
        #iterate through the words strs
        for words in strs:
            #start a count * 26 to map the location of where it is
            count = [0] * 26
            #iterate through each letter in the words
            for letters in words:
                #access count and now to ord(letter) - ord("a") +=1 
                #we add 1 to map it to the location
                count[ord(letters) - ord("a")] += 1
                #convert it to a tuple name it key
            key = tuple(count)
                #check if key in storage
            if key not in storage:
                #create a new list with the key
                storage[key] = []
            #append to that key the count
            storage[key].append(words)
        return list(storage.values())
