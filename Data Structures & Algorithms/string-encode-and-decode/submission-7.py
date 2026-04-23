class Solution:

    def encode(self, strs: List[str]) -> str:
        #first store in a string
        encoded = ""

        #iterate through each word in strs
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        #store the resutl
        result = []

        #start a pointer
        i = 0
        #start the loop
        while i < len(s):
            #start another pointer here 
            j = i
            #now look for the #
            while s[j] != "#":
                j += 1
            #now that we find it
            #this is just the int
            length = int(s[i:j])
            #now move that and append to the result
            result.append(s[j+1 : j+1+length])
            #now move i
            i = j + 1 + length
        return result
