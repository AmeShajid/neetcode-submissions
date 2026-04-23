class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #set a dictionary because it gets rid of dupilcates
        countS = {}
        countT = {}

        #Check letters inside string
        for letter in s:
            #check if letters is not in there make it = 1
            if letter not in countS:
                #set to 1
                countS[letter] = 1
            #add +1
            else:
                countS[letter] +=1

        for letter in t:
            #check if letters is not in there make it = 1
            if letter not in countT:
                #set to 1
                countT[letter] = 1
            #add +1
            else:
                countT[letter] +=1
        return countS == countT



        
        