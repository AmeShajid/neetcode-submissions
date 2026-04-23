class Solution:

    def encode(self, strs: List[str]) -> str:
        #first we need to encode this string
        encoded = ""
        #iterate through str
        for s in strs:
            #to encode to the len word + # + word
            encoded += str(len(s)) + "#" + s
        #return encode
        return encoded

    def decode(self, s: str) -> List[str]:
        #so now we need to hold a result
        result = []

        #start a pointer from the beginning 
        i = 0
        #start a loop unitl the end of the encoded wodr
        while i < len(s):
            #start a second pointer starting from i 
            j = i
            #while the position does not equal # 
            while s[j] != "#":
                #continue moving forwards
                j += 1
            #when we find the number
            #our length is int slice of that
            length = int(s[i:j])
            #so now slice the world from j+1 until j+1+length
            result.append(s[j+1 : j+1+length])
            #move i forward 
            i = j+1+length
        return result

