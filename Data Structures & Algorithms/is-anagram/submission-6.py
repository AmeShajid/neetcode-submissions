class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if string is anagram
        #return false if not true

        #have a dictionary for both strings
        #dictionary s string
        s_storage = {}
        #dictionary t string
        t_storage = {}

        #iterate through string s
        for letter in s:
            #if letter in dictinary s 
            if letter in s_storage:
                #append 1 to count
                s_storage[letter] += 1
            #else initate count with 1
            else:
                s_storage[letter] = 1
        #print(dictonary s)
        print(s_storage)

        #iterate through string t
        for letter in t:
            #if letter in dictinary t
            if letter in t_storage:
                #append 1 to count
                t_storage[letter] += 1
            #else initate count with 1
            else:
                t_storage[letter] = 1
        #print(dictonary t)
        print(t_storage)

        if s_storage != t_storage:
            return False
        return True
        