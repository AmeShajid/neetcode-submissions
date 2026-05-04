class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #first have a pointer for t
        t_index = 0
        #iterate through each letter in s
        for char in s:
            #if len of t and current index match
            if len(t) == t_index:
                #break
                break
            #if pointer nad the index position in s is same
            if char == t[t_index]:
                #move index pointer 1 
                t_index += 1
        #whatever is left from len t - pointer is what we append
        return len(t) - t_index

        