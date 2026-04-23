class Solution:

    def encode(self, strs: List[str]) -> str:
        #first store the encoded string
        encoded = ""
        #iterate through encoded with s 
        for s in strs:
            #add to encoded with str len of s + # + s
            encoded += str(len(s)) + "#" + s
        #return encoded
        return encoded

    def decode(self, s: str) -> List[str]:
        #we need to return a list
        result = []
        #start a pointer so we can keep track of slices
        i = 0
        #start a while loop until len of s
        while i < len(s):
            #so now start a second pointer to find the length of the word
            j = i
            #keep adding one until we get to the #
            while s[j] != "#":
                j += 1
            #if we found the # this is the length of the words
            length = int(s[i:j])
            #so now we need to append to result
            #slice from j+1 until j+1+length thats the entire word
            result.append(s[j+1 : j+1+length])
            #now move i from j+1+length because thats the new set
            i = j+1+length
        #return result
        return result
