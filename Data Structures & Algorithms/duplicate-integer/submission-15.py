class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #first we will need a storage to store our seen numbers
        storage = {}

        #next we need to iterate through nums
        for num in nums:
            #check if we have seen this number inside of our storage
            if num in storage:
                #if we have then return True
                return True
            #else 
            else:
                #add it to our storage
                storage[num] = 1
        #if we pass everything retun False
        return False
        