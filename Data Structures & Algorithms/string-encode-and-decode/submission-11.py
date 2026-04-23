class Solution:

    def encode(self, strs: List[str]) -> str:
        #first store in a string
        encoded = ""

        #iterate through each word in strs
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        #we need to save the result in a list
        result = []
        #now we need to set a pointer so we can iterate
        i = 0
        #now start iteraing until the string is done
        while i < len(s):
            #now set another point 
            j = i
            #now find the number first 
            while s[j] != "#":
                #go up by 1 if we dont find it
                j += 1
            #now that we ahve the number make that the length
            length = int(s[i:j])
            #now we need to move the length
            #so first +1 to move past the # then same until the legnth tho
            result.append(s[j+1 : j+1+length ])
            #now we need to update the i so move past the entire word
            i = j+1+length
        return result

