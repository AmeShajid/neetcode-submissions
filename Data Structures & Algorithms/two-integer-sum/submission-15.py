class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #storage for nums
        storage = {}

        #iterate through nums
        for index, value in enumerate(nums):
            #get the goal number 
            goal = target - value
            #if goal is in storage
            if goal in storage:
                #return goal index and index
                return [storage[goal], index]
            #else
            else:
                #switch the index and value 
                storage[value] = index
        #return 
        