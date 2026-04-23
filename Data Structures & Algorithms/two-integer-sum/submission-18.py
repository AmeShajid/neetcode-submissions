class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #storage for nums
        storage = {}

        #iterate through list with both index n value
        for index, value in enumerate(nums):
            #get a goal numbe 
            goal = target - value
            #check if teh goal in storage
            if goal in storage:
                return [storage[goal], index]
            #else
            else:
                storage[value] = index
        