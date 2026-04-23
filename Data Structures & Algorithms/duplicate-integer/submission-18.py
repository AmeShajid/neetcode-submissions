class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return true if any value appears more than once in the array
        #return false if any value appears once in teh array

        #first storage for nums
        storage = {}

        #iterate through nums
        for num in nums:
            #check if its inside storage
            if num in storage:
                #if inside of storage 
                return True
                    #return True
                #else
            else:
                #add it to the dict
                storage[num] = 1
        #return false
        return False
                
        