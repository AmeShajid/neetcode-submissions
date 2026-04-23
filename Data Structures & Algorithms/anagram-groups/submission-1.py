class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #store in empty dictionary
        words = {}
        #iterate through each words
        for word in strs:
            #create a list of 26 zeros for a-z
            char_count = [0] * 26
            #iterate through letters in the words
            for char in word:
                #covert char to index
                char_count[ord(char) - ord("a")] += 1
            #covert the list to a tuple so it can be a key
            key = tuple(char_count)
            #if the key is not in the list create a new list
            if key not in words:
            #append the word to the dictionary
                words[key] = []
            words[key].append(word)
        #return the dictionary as a list
        return list(words.values())