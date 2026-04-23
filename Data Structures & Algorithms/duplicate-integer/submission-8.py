class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #return true if value appears more than once
        #return False if only once

        #store numbers in dictionary
        storage = {}
        #iterate through list
        for num in nums:
            #check if number in storgae
            if num in storage:
                #if it does return True
                return True
            #else add it with equal to one
            else:
                storage[num] = 1
        #return False
        return False




        

