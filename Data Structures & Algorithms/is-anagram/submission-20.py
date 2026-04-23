class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #time - o(n) going through nums
        #space - o(n) would be 2n beucase we make 2 storage but coeff doesnt matter
        #first if both len arent right then wrong
        if len(s) != len(t): 
            return False

        #create two dicts 
        string_s = {}
        string_t = {}

        #iterate through string
        for letter in s:
            #if letter in storage:
            if letter in string_s:
                #add 1 to the letter counter
                string_s[letter] += 1
            #else
            else:
                #add the letter with count 1
                string_s[letter] = 1
        
        #iterate through string
        for letter in t:
            #if letter in storage:
            if letter in string_t:
                #add 1 to the letter counter
                string_t[letter] += 1
            #else
            else:
                #add the letter with count 1
                string_t[letter] = 1
        
        #if both lens aren't equal retunr flase
        if string_s != string_t : 
            return False
        return True
        
