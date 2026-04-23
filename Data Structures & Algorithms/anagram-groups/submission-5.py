class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we will store all of the sorted anagram pairs here
        result = {}

        #iterate through strs
        for s in strs:
            #to start our count we start off with 0 * 26(leters in alphabet)
            count = [0] * 26
                #go through every single chracter in each string
            for letter in s:
                #this is where we start mapping evertything for our count
                #to get inside count to ascii - ascii(a)
                #this will tell us the position to put it in
                count[ord(letter) - ord("a")] += 1

            #convert it into a tuple
            key = tuple(count)

            #check if it is inside result
            if key not in result:
                #if it doesn't exist create a new list and append to that list
                result[key] = []
            result[key].append(s)
        #return as a list and only the values of result
        return list(result.values())
        



        