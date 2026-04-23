class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return True if value appears more than once
        #return False if values appears once

        #store the values
        storage = {}
        #iterate through nums
        for num in nums:
            #If num is in our storage 
            if num in storage:
                #return True
                return True
            #else
            else:
                #add this to our storage with a value of one
                storage[num] = 1
        return False
         