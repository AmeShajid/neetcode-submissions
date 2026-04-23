class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #first we need to store the words
        storage = {}
        #iterate through the words in strs
        for words in strs:
            #start a count to map the letters
            count = [0] * 26
            #iterate through letters in words
            for letters in words:
                #enter count do ascii letter - ascii a and add 1 to that
                count[ord(letters) - ord("a")] += 1
            #conver the count to a tuple
            key = tuple(count)

            #check if the key is in storage
            if key not in storage:
                #if not then make a new list for the key 
                storage[key] = []
            #then append words to that key
            storage[key].append(words)
            #only return values
        return list(storage.values())
        