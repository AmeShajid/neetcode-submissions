class Solution:

    def encode(self, strs: List[str]) -> str:
        #store encoded string 
        encoded = ""
        #iterate through string
        for s in strs:
            #get len of string + # + s
            encoded += str(len(s)) + "#" + s
            print(encoded)
        return encoded

    
    def decode(self, s: str) -> List[str]:
        #we need a list of strings
        result = []
        #need a pointer i for what position we are in for string
        i = 0

        #iterate through chracters while i < len(str)
        while i < len(s):
            #set another pointer to find the end of delimiter
            j = i
            #the chracter for j doesn't equal # means we are still at an integer
            while s[j] != "#":
                #add 1 until we find a #
                j +=1
            #once we get to the # we knwo that the lengh is between i and j which is just the number chracter
            #this tells us how many chracters we have to read
            length = int(s[i:j])
            #start at j+1 because thats the first chrarcter in the word
            #here we are starting from j+1 and then unti the end of string
            #and also appened this to result
            result.append(s[j+1 : j + 1 + length])
            #how to increment i once one word is done go to the next
            #this is the beginnign of the next string
            i = j + 1 + length
        return result




