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
        #store result list
        result = []

        #start a pointer
        i = 0

        #loop through strs
        while i < len(s):
            #start a secondary pointer so we can find len
            j = i
            #while it doesnt equal 3
            while s[j] != "#":
                j += 1
            #if we find it
            length = int(s[i:j])

            #append to result
            result.append(s[j+1 : j+length + 1])

            #move the poionter
            i = j+1+length

        #reselt
        return result
