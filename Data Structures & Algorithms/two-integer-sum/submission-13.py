class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the indices of i and j that nums[i] + nums[j] == target

        #so first we need to store the numbers we see
        storage = {}

        #iterate through nums with both the key and value
        for index, value in enumerate(nums):
            #the goal is going to always change because we are iteraing
            goal = target - value
            #if goal is in storage return that
            if goal in storage:
                return [storage[goal], index]
            #that means its not in it
            else:
                #since we are returning the index
                #we need to fliup how we store these
                storage[value] = index