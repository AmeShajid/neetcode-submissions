class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all of them into sublists where they all match
        #return in any order

        #we need to store these
        #the key will be the letters, and the values will be the words
        storage = {}

        #first iterate through the lists
        for word in strs:
            #now we need to creat the letter count
            #its going to be 26 empty 0 for each letter
            count = [0] * 26
            #now iterate for each letter in word
            for letter in word:
                #so now that we have the letter
                #we need to set a mapping for htis
                #first access count and then do the ord then add a 1 to that position
                count[ord(letter) - ord("a")] += 1
            #now we need to make a tuple out of the count to make it into a group
            key = tuple(count)
            #Now check if the key is in our storage
            if key not in storage:
                #if its not in there add it to storge as an empty list
                storage[key] = []
            #else appennd it to the storage
            storage[key].append(word)
        #now return all the values from the storage as a list
        return list(storage.values())