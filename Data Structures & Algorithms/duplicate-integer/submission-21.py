class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #store the numbers
        storage = {}

        #iterate through each num
        for num in nums:
            #if num in storage return true
            if num in storage:
                return True
            #else its false add it and rturn false
            else:
                storage[num] = 1
        return False
        