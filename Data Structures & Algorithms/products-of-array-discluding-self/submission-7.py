class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we need a placeholder for each answer
        result = [1] * len(nums)    

        #so now we need to iterate through nums
        for i in range(len(nums)):
            #so now start a count for the total left product
            left_product = 1
            #so nowiterate from the beginning to the current number
            for j in range(0, i):
                left_product *= nums[j]
            
            #so now do the same for rigth
            right_product = 1
            #now start from i+1 to the end 
            for k in range(i+1, len(nums)):
                right_product *= nums[k]
            
            #so now we need to get teh total product 
            total_product  = left_product * right_product

            #for every iteration replcae the total product
            result[i] = total_product
        return result