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
            #iterate through values i passed 
            for j in range(i):
                #calculate left product 
                left_product = left_product * nums[j]

            #right product
            #iterate through nums with +1 and until the end of nums
            for k in range(i+1, len(nums)):
                #calculate right product
                right_product = right_product * nums[k]

            #calculate total_product
            total_product = left_product * right_product
            
            #replace the values of result with total_product
            result[i] = total_product
        return result
            

            


