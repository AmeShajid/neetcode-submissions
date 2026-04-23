class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first we need to store results
        result = [1] * len(nums)

        #so now iterate through nums
        for i in range(len(nums)):
            #so now get the left product everytime we iterate
            #first set left product
            left_product = 1
            #iterate only for left products
            for j in range (0 , i):
                #just multiply all the numbers for numsj
                left_product *= nums[j]
            
            #now do the same for right
            right_product = 1
            for k in range(i+1, len(nums)):
                right_product *= nums[k]
            
            #now get the total product multiply both
            total_product = left_product * right_product
            #then update results
            result[i] = total_product
        return result

        