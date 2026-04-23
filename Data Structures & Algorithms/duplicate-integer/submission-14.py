class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return True if any value appears more than once in the array 
        #return False if if all values appear once

        #first we need to store the numbers when we see them
        storage = {} 

        #now we need to iterate through nums
        for num in nums:
            #check if the number is already in storage
            if num in storage:
                #return True
                return True
            #if it isnt then 
            else:
                #add it to storage with a 1
                storage[num] =1
        return False
        