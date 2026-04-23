class Solution:

    def encode(self, strs: List[str]) -> str:
        #we need to hold our string
        encoded = ""
        #iterate through the list
        for s in strs:
            #for our holder do the len of the str + the # plus the word
            encoded += str(len(s)) + "#" + s
        #return string
        return encoded

    def decode(self, s: str) -> List[str]:
        #store for result
        result = []
        #first set a pointer so we know where we are
        i = 0
        #now do a while loop until we are at the first number
        while i < len(s):
            #start a second pointer to get the number
            j = i
            #if j doesn't equal # then keep going
            while s[j] != "#":
                j +=1 
            #make this into an int
            length = int(s[i:j])
            #so now we need to slice this word and then move i again
            result.append(s[j+1 : j+1+length])
            #now move i
            i = j+1+length
        return result

