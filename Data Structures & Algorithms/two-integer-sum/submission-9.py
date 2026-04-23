class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the indicies i and j so it equals target
        #i and j cannot be the same

        #storage to store the key:value
        storage = {}

        #iterate through nums with key and value
        for key, value in enumerate(nums):
            #we need to get a goal = target - value
            goal = target - value
            #if our goal is in the storage
            if goal in storage:
                #return the stoarge[goal] index value and the other key
                return [storage[goal], key]
            else:
                #add the stoage[value] and add the index value
                storage[value] = key

        