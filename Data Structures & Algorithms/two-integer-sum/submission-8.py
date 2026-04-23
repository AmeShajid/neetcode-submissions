class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #return index values of i and j that == target
        #i and j cannot be the same

        #store the numbers we iterate through
        storage = {}

        #iterate through nums with both index and value
        for index, value in enumerate(nums):
            #check for the goal ( goal = target - value)
            goal = target - value
            #if our goal is in storage
            if goal in storage:
                #return the storage[goal] and index
                return [storage[goal], index]
            #else
            else:
                #add this value with its index to storage
                storage[value] = index
                print(storage)
        