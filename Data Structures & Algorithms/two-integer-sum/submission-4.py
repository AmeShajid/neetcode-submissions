class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return index values of the two numbers == target
        #index values cannot be the same

        #dictionary for storing numbers
        # i : n
        storage = {}

        #iterate through list but also grab value and index
        # i = key
        # n = value
        for i , index in enumerate(nums):
            #find the difference we need to find
            difference = target - index
            #check if difference inside the hashmap 
            if difference in storage:
                #if it is return paur
                return [storage[difference], i]
            #if we dont add to the hasmap
            storage[index] = i
        return 


