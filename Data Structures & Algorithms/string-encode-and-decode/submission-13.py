class Solution:

    def encode(self, strs: List[str]) -> str:
        #we need to first encode this into one big string
        encoded = ""
        #so now iterate through everything in the list
        for s in strs:
            #add it like this string length of word and then the # then word
            encoded += str(len(s)) + "#" + s
        #dont forget to return encoded
        return encoded

    def decode(self, s: str) -> List[str]:
        #so now we need to decode this string
        #hold the result in a list
        result = []

        #so now we need a pointer to keep track of our positions
        i = 0
        #so now iterate trhough this encoded word
        while i < len(s):
            #so now start another pointer so we can get the lenght of the string
            j = i
            #so now we want to move j until we find the # 
            while s[j] != "#":
                j += 1
            #so now that we have the number we want to set this to the length 
            length = int(s[i:j])

            #so now that we have the length we need to cut this string 
            #add it to the result
            #first move from j+1 to move past the # then do j+1 + length becasue thats the stirng length
            result.append(s[j+1 : j+1+length])
            #so now we need to move i
            #just move i j+1 + length thats the entire word now we do the next word
            i = j+1+length 
        return result
