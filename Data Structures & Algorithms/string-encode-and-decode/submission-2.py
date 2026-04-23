class Solution:

    def encode(self, strs: List[str]) -> str:
        #store the encoded string in a string
        encoded = ""
        #iterate through strs to encode 
        for s in strs:
            #our encoded will be the string len of strs + # + s
            encoded += str(len(s)) + "#" + s
            print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        #store result in a list
        result = []

        #keep track of position  while iterating
        i = 0

        #since we dont know exact position just do a while loop
        while i < len(s):
            #we need another variable to swap with so we can track position
            j = i
            #here we need to find the delimiter so keep iterating until we find it
            while s[j] != "#":
                j += 1
            #once its found thats the length of our words
            length = int(s[i:j])
            
            #so now we want to append this to the result
            #we want to do starting from j+1 because thats a letter
            #until j+1 + length becuase thats teh full word
            result.append(s[j+1 : j + 1 + length])
            #and then we have to update the position of i to the next word
            i = j + 1 + length 
        return result





