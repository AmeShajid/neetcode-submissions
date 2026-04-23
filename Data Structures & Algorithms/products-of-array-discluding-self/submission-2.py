class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)  # create result list with 1's
        
        # we loop through both index (i) and value (num) together
        for i, num in enumerate(nums):
            left_product = 1
            right_product = 1

            # multiply everything to the left of index i
            for j in range(0, i):
                left_product = left_product * nums[j]

            # multiply everything to the right of index i
            for k in range(i + 1, len(nums)):
                right_product = right_product * nums[k]

            # total product is left * right
            total_product = left_product * right_product

            # store it in result[i]
            result[i] = total_product
        
        return result