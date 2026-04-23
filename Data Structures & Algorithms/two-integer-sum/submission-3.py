class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Dictoinary to store value and index
        nums_dictionary = {}
        #iterate through all of nums grab both key and value
        for i, index in enumerate(nums):
        #Difference = target - current number
            difference = target - index
        #if the difference is in our dictoinary
            if difference in nums_dictionary:
        #we want to return the dictionary value and index
                return [nums_dictionary[difference],i]
            nums_dictionary[index] = i






        

