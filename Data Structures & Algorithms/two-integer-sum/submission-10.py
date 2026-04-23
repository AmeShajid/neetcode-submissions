class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the indices i and j == target
        #i cannot equal j
        
        #storage to keep number and position
        storage = {}

        #iterate through each num with both index and value
        for index, value in enumerate(nums):
            #set the new goal(goal = target - value)
            goal = target - value
            #if the goal is in the storage 
            if goal in storage:
                #return teh index value alongside the index
                return [storage[goal], index]
            #else add this value to the storage
            else:
                storage[value] = index
            