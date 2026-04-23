class Solution:
    #encoded method is len of string + # plus string

    def encode(self, strs: List[str]) -> str:
        #so first we need to store the new string
        encoded = ""
        #now we need to fill the string
        #iterate through the string
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        #we need to store the result
        result = []

        #start a pointer 
        i = 0
        #now iterate trhough the words until we find the #
        while i < len(s):
            #start a new pointer
            #have j take over for i
            j = i
            #now we need to find the #
            while s[j] != "#":
                #add 1 until we find it
                j += 1
            #once we find it
            #our new length is the string from i to j
            #i is that at the beginning j beging up to the #
            length = int(s[i:j])

            #now append this string to the result 
            result.append(s[j+1 : j+1+length])
            #now move i to the next wrod
            i = j + 1 + length
        return result




