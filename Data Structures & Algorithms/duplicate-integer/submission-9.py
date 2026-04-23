class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return True if value appears more than once
        #return False if value shows up ones

        #store numbers
        storage = {}

        #iterate through nums
        for num in nums:
            #check if nums in storage
            if num in storage:
                #if it is return True
                return True
            #else add it to storage 
            else:
                storage[num] = 1
        #return False cause its only once
        return False
         