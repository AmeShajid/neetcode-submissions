class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return True if any value appears more than once in teh array
        #return False if value appears once

        #keep track of whats been seen, store them
        storage = {}

        #iterate through nums
        for num in nums:
            #if the value is in storage then return false
            if num in storage:
                return True
            #else just add it to the storage with a 1 
            else:
                storage[num] = 1
        return False
        
        