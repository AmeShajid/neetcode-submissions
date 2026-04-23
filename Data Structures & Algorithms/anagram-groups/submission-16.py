class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all anagrams together

        #so first we need to create a dictionary
        #the key is going to the count of the letters the value will be the actual letters
        storage = {}

        #so now we need to iterate through this list
        for word in strs:
            #so now create a count of 26 letters
            count = [0] * 26
            #so now iterate through each letter in words
            for letter in word:
                #now we need to change the value for count
                #we want to do a - letter and that add a 1 to that position 
                count[ord("a") - ord(letter)] += 1
            #so now once we have that we want to create a tuple out of that count for all the ones that fit
            key = tuple(count)
            #so now we want to check if this key is in the sotrage
            if key not in storage:
                #if it is not in it then we want to add an empty list to this position
                storage[key] = []
            #now for the words that match this key append it to this key
            storage[key].append(word)
        #now we want to only return the values as a list
        return list(storage.values())
        