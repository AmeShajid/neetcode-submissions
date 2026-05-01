class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #set two pointers start from 0 
        i = 0
        j = 0

        #so now iterate until the bigger string is done
        while j < len(t):
            #if we match on both i and j then move i one
            if i < len(s) and s[i] == t[j]:
                i +=  1
            #now move j 1
            j += 1
        #so now if all of them matched 
        return i == len(s)

        