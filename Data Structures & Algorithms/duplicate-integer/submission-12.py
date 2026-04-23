class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return True = value appears more than once
        #return False = value appears once
        #first have a storage for the value that are seen
        storage = {}
        #iterate through nums 
        for num in nums:
            #check if it is in our dictionary
            if num in storage:
                #return true 
                return True
            else:
                #add it to the dicitionary and make it equal one as a holder
                storage[num] = 1
        #return False
        return False

         