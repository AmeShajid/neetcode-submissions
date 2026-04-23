class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #list with numbe 1 place holder
        result = [1] * len(nums)

        #iterate through nums
        for num in range(len(nums)):
            #set product scores to 1
            left_product = 1
            right_product = 1

            #iterate from 0 to current i 
            for left_pointer in range(0, num):
                #update product 8 nums left pointer
                left_product *= nums[left_pointer]
            
            #iterate from i+1 to len of nums
            for right_pointer in range(num+1, len(nums)):
                #update product in nums right pointer 
                right_product *= nums[right_pointer]

            #get a total product multiply both products
            total_product = left_product * right_product
            #update result by replacing each num with its total
            result[num] = total_product
        return result
        