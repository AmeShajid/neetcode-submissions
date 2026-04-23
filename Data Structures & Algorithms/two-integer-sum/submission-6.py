class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #track these numbers in dictionary
        #index : value
        storage = {}
        #iterate through nums with both index and value
        for index, value in enumerate(nums):
            #find goal from target - value
            goal = target - value
            #if goal in storage:
            if goal in storage:
                #return the goal and index
                return [storage[goal], index]
            #else append the storage value with index
            else:
                storage[value] = index


