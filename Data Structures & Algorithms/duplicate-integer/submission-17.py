class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return True if any value appears more than once 
        #return False if all values appear once

        #store all the nums
        storage = {}

        #iterate through nums
        for num in nums:
            #if num in storage:
            if num in storage:
                #return True
                return True
            #else:
            else:
                #add it to storage with a 1 value
                storage[num] = 1
        #return False
        return False 