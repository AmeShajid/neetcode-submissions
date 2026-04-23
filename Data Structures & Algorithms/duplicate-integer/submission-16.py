class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #storage to know what we have seen
        storage = {}
        #iterate through nums
        for num in nums:
            #if num in storage 
            if num in storage:
                #return True
                return True
            #else
            else:
                #Add it to storage
                storage[num] = 1
        #return False
        return False
        