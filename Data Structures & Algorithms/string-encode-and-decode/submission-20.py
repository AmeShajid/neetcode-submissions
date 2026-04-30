class Solution:

    def encode(self, strs: List[str]) -> str:
        #stoarge for string
        encoded = ""

        #iterate through strs
        for s in strs:
            #add len of s + # + s
            encoded += str(len(s)) + "#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        #store result in list
        result = []
        #start a pointer 
        i = 0
        #iterate through the until we reach the end 
        while i < len(s):
            #start a second pointer 
            j = i
            #loop until we reach the #
            while s[j] != "#":
                #move +1
                j +=1 
            #that means we found it thats the length 
            length = int(s[i:j])
            #now we need to append to result this word 
            word = s[j+1 : j+1+length]
            result.append(word)
            #now move the pointer 
            i = j+1+length 
        return result
