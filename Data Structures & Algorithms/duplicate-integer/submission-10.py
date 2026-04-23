class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return true if any value appears more than once
        #return false if all values are once

        #store the numbers
        storage = {}
        #iterate through the numbers
        for num in nums:
            #check if the numbers in our storage
            if num in storage:
                #if it is return true
                return True
            #else update the position to one
            else:
                storage[num] = 1
        #return false
        return False
         