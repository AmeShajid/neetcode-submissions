class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return i and J such that nums[i] + nums[j] == target
        #i != j

        #store the numbers
        storage = {}

        #iterate through nums with index and value
        for index, value in enumerate(nums):
            #define goal 
            goal = target - value
            #if our goal is in storage
            #return [storage[goal], index]
            if goal in storage:
                return [storage[goal], index]
            #else add it to the storage
            else:
                #add the index to teh value
                storage[value] = index
        return

        