class Solution:

    def encode(self, strs: List[str]) -> str:
        #we need to store the encoded string in a string
        encoded = ""
        #Now iterate through each string 
        #our idea is for each letter get the length then # then string
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        #first we need to store this somewher
        result = []
        #so now we need to set a potiner
        i = 0
        #iterate through each letter until are all doen
        while i < len(s):
            #set a another pointer so we can get the number
            j = i
            #now iterate until we see the #
            while s[j] != "#":
                #add 1 until we see it
                j += 1
                #now set the length of the string to this 
            length = int(s[i:j])

            #now we need to move this 
            #first do j+1 to move past the $ then we do j+1 + length to get the entire word
            result.append(s[j+1 : j+1+length])
            #so now we need to move i to the next owrd
            i = j+1+length
        return result
