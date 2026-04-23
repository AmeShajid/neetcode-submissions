class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #return all anagrams in groups

        #store the words in dictionary
        storage = {}
        #iterate through strs
        for words in strs:
            #make character count for a -z
            char_count = [0] * 26
                #iterate through the words in strs
            for letters in words:
                #index these values
                #ascii - ascii a += 1
                char_count[ord(letters) - ord("a")] += 1

            #convert this list into a tuple
            key = tuple(char_count)

            #check if this key is inside storage 
            if key not in storage:
                #we want to make a new list and then appened
                storage[key] = []
            storage[key].append(words)
        return list(storage.values())
