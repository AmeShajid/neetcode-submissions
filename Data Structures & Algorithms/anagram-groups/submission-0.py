class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all anagrams together into one list

        #create an empty dicrtionary to store 
        words = {}
        #iterate through each word in strs
        for word in strs:
            #sort the word to see if it matches
            sorted_word = "".join(sorted(word))

            # If the key is not in the dictionary, create a new list
            if sorted_word not in words:
                words[sorted_word] = []
            #append the orignal word as the value
            words[sorted_word].append(word)

        #return the group words as a list
        return list(words.values())
        