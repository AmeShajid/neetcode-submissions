class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the index values of i and j that equal target

        #store the values
        #index : value
        storage = {}
        #iterate through the values get key and value
        for index,value in enumerate(nums):
            #find the goal -> goal = target - value
            goal = target - value
            #if goal in storage:
            if goal in storage:
                #return the goal index, and the regualr index
                return [storage[goal], index]
            #else if it is not 
            else:
                #add the value to the storage with the index too
                storage[value] = index
        