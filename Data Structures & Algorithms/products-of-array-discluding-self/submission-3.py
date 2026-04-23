class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create the result list with 1's repopulate later
        result = [1] * len(nums)

        #iterate through nums with both index and value
        for index, value in enumerate(nums):
            #have the left and right set to one for multipication purposes
            left_product = 1
            right_product = 1

            #multiply everything to the LEFT of index
            #so range should be start from 0 to i for every left
            for j in range(0,index):
                left_product = left_product * nums[j]

            #multiply everything to the RIGHT of index
            #so range should start from i+1 until len(nums)
            for k in range(index+1, len(nums)):
                right_product = right_product * nums[k]

            #get the total product = left * right
            total_product = left_product * right_product

            #store these results 
            result[index] = total_product
        return result
