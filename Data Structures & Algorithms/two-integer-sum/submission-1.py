class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initlaize pointer to get index value
        i = 0

        #initlaize dictoinary so we can get both key and index pair
        num_dict = {}

        #here we are going to fill the dictionar
        for num in nums:
            #we made it = i so we can have the value pair be in the index
            num_dict[num] = i
            #then continue through all of nums
            i += 1

        #range is just index values
        for i in range(len(nums)):
            #goal is our target(7) - nums[i](3) = 4
            goal = target - nums[i]
            # if 4 in dictionary
            if goal in num_dict and i != num_dict[goal]:
                #return [index value, index value 2]
                return [i, num_dict[goal]]
