class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #create a storage to store numbers
        storage = {}
        
        #iterate through nums with both index and value
        for index, value in enumerate(nums):
            #create a goal comes from goal = Target - value
            goal = target - value
            #if our goal is in storage 
            if goal in storage:
                #return goal index and curent index
                return [storage[goal], index]
            #else
            else:
                #since we are returning indexes we need to store value = index
                storage[value] = index
        return 
        