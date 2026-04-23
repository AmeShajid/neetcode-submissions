class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return index values of the values that equal the target and from least to greates

        #first create a storage, we need to flip the value and index
        storage = {}
        
        #iterate through nums with value and index
        for index, value in enumerate(nums):
            #we need to find the goal number based on the current number 
            goal = target - value
            #if the goal is inside of our storage
            if goal in storage:
                #return the current index and the index from teh storage 
                return [storage[goal], index]
            #else
            else:
                #its not inside and we need to store the number flipped
                storage[value] = index
