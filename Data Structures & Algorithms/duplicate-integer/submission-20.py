class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return True if value appears more than once in nums
        #return False if value appears once in nums

        #time - o(n) - iterate n times
        #space - o(n) - becuase we store everything from nums

        #storage for keeping track whats inside
        storage = {}

        #iterate through nums
        for num in nums:
            #if the num in storage:
            if num in storage:
                #return True
                return True
            #else
            else:
                #add the curr number to stoarge 
                storage[num] = 1
        #return false
        return False