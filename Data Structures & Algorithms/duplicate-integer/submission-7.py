class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #retrun True if any value appears more than once
        #return False if value appears once

        #store all the numbers from nums in a dictionary
        storage = {}
        #iterate through nums list
        for num in nums:
            #check if its already in nums
                if num in storage:
                #if it is return True
                    return True
            #if not add it to dictionary and make the value 1
                else:
                    storage[num] = 1
        #return False because we didn't find any dupilcates
        return False
         