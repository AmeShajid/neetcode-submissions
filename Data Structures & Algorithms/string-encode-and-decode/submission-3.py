class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
            print(encoded)
        return encoded

    
    def decode(self, s: str) -> List[str]:
        #first we need to store result
        result = []
        #we need to set our start
        i = 0
        #we need to iterate until its more then the len of our s
        while i < len(s):
            #we need to start our second pointer
            j = i
            #we need to iterate until j == #
            while s[j] != "#":
                #move it up one
                j += 1
            #then we know this is the length of the word
            length = int(s[i:j])
            #append this to the list and slice
            result.append(s[j+1 : j+1+length])
            #set the new location of i
            i = j + 1 + length
        return result
            
            
