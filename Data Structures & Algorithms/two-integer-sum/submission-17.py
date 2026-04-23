class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #get the first number
        #subtract first number from target number (goal)
        #check if the goal is in the list
        #if its not move onto the next number
        #repeat and return as a list
        #
        
        #for index, value in enumerate(nums):
        #    number = target - value
        #    if value in nums:
        #        return [index, ]


        #store the numbers in a dict
        storage = {}
        #iterate through nums
        for index, value in enumerate(nums):
            #get a gaol val from nums target - val
            goal = target - value
            #if the goal is in storage
            if goal in storage:
                #return index, storage index
                return [storage[goal], index]
            #else
            else:
                #add value to storage
                storage[value] = index
        #return 