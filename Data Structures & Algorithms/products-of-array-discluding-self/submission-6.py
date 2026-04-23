class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we need to create a list so we can hold the multiple values
        result = [1] * len(nums)

        #now iterate through nums
        for i in range(len(nums)):
            #so now we need to iterate through the right side
            #first set it to 1
            left_product = 1
            #now iterate only the left side from 0 to current i
            for j in range(0, i):
                left_product *= nums[j]
                
            #now we need to iterate through the left siee
            #set rigth product to 1
            right_product = 1
            #now iterate through but i+1 untril the end
            for k in range(i+1, len(nums)):
                right_product *= nums[k]
            
            #now find the total product 
            total_product = left_product * right_product
            #now we need tro popualte the result
            result[i] = total_product
        return result