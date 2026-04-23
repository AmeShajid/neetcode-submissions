class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #first get our results size of nums
        result = [1] * len(nums)

        #iterate through nums with range
        for i in range(len(nums)):
            #set right and left product to 1
            left_product = 1
            right_product = 1
            
            #left product
            #right to left
            for j in range(i-1, -1, -1):
                left_product = left_product * nums[j]

    
            #right product
            #right to left
            # not 4 * 6 do 6 * 4
            for k in range(len(nums)-1, i, -1):
                right_product = right_product * nums[k]

            #calculate total_product
            total_product = left_product * right_product
            
            #replace the values of result with total_product
            result[i] = total_product
        return result
            

            


