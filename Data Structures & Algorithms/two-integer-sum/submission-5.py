class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the index values of i and j 
        #i and j cannot equal each other

        #dictoinary for number storage
        #index : value
        storage = {}
        #iterate through nums with key and value use enumerate
        for index, value in enumerate(nums):
            #find goal in the list
            goal = target - value
            #if goal is in storage:
            if goal in storage:
                #return storage index and i
                return [storage[goal], index]
            #if not add the value to the dictinary with index value
            else:
                storage[value] = index
        return