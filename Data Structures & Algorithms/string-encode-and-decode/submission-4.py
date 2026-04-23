class Solution:

    def encode(self, strs: List[str]) -> str:
        #first we need to store encoded string
        encoded = ""

        #iterate through s and add the holders
        for s in strs:
            encoded += str(len(s)) + "#" + s
            print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        #we need to store our result
        result = []
        #we need a place holder
        i = 0
        #we need to iterate until we are done with the entire string
        while i < len(s):
            #we need to have another value place holder to get the full lenght of the string
            j = i
            #make sure we stop until the #
            while s[j] != "#":
                j += 1
            #set this to our length so convert that slice into an integer
            length = int(s[i:j])
            #append this to our result start at j+1 until j+1+length
            result.append(s[j+1 : j+1+length])
            #set i to our new position j+ 1 + length
            i = j+1+length
            #return result
        return result
