class Solution:
    def scoreOfString(self, s: str) -> int:

        #Time = o(n) - iterating through every n
        #space = o(1) - constant because its just 1 loop 1 var
        #result var
        result = 0

        #iterate through len of nums
        for i in range(len(s)-1):
            #make curr var and next var into an ord add to res
            result += abs(ord(s[i]) - ord(s[i+1]))
        #return result
        return result
        