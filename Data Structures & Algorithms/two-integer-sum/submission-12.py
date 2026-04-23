class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the indices i and j such that nums[i] + nums[j] == target
        #i cannot == j

        #we need to sotre these numbers first
        storage = {}

        #iterate through nums with both index and value
        for index, value in enumerate(nums):
            #now we need to set a goal 
            goal = target - value
            #if our goal is in storage then return that number
            if goal in storage:
                return [storage[goal],index]
            #else add the index to the storage with its value
            else:
                storage[value] = index
        return