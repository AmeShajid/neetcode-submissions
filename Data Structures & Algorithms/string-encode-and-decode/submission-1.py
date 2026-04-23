class Solution:

    def encode(self, strs: List[str]) -> str:
        #we want to store the encoded stirng
        encoded = ""

        #iterate through string
        for s in strs:
            #get len of string + # + s
            encoded += str(len(s)) + "#" + s
            print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        #our result is a list of string
        result = []
        #to keep track of where our letter is 
        i = 0

        #iterate through while our chracters are less than len(strs)
        while i < len(s):
            #set another pointer so we can the #
            j = i
            #so here it means we are still at a number because before a # its the number
            while s[j] != "#":
                #we add 1 until we find the #
                j += 1
            #the length of our official string is just the chracters from i to j which is just the number
            length = int(s[i:j])
            #so now append to the result
            #access s and now we want to do j+1 becuase thats teh first letter
            #and then until j+1 + length  thats the full words
            result.append(s[j+1: j+1 + length])
            #for the next words just move i j +1 + length and thats teh next word and contine
            i = j + 1 + length
        return result

