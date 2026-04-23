class Solution:

    def encode(self, strs: List[str]) -> str:
        #store our encoded message in a string
        encoded = ""
        #iterate through each letter 
        for s in strs:
            #add the new encoded message to the encoded stirng
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        #store result in a list because we return a list
        result = []
        #start a counter 
        i = 0
        #iterate until we are done with the entire string
        while i < len(s):
            #start a new place holder to get length of the piece
            j = i
            #loop with j until we find the delimiter whihc is #
            while s[j] != "#":
                #add one until it finds it
                j += 1
            #make the length equal to that value
            length = int(s[i:j])

            #append this to our list now
            #first slice : first start of letter
            #second slice : all the way to the end of the string
            result.append(s[j+1 : j+1+length])

            #update value of i to the end of the string now
            i = j+1+length
        return result

        
