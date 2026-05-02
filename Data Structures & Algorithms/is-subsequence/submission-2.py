class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #first start two pointers
        i = 0
        j = 0
        #loop through the longer one
        while j < len(t):
            #if the pointer for hte shorter one still in range AND the index values are the smae
            if i < len(s) and s[i] == t[j]:
                #for i do +1
                i += 1
            #for j to +1
            j += 1
        #return if i == len(s)
        return i == len(s)
        