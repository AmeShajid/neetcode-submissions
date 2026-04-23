class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create the result list with 1s so we can populate later
        result = [1] * len(nums)

        #iterate through nums with range 
        for i in range(len(nums)):
            #lets to the right first 

            #set left product == 1 so we can multiply
            #also when it is empty space its basically a one
            left_product = 1
            #iterate again but this time starting from 0 and until 
            for j in range(0, i):
                #left product == left product * current num
                left_product = left_product * nums[j]
            
            #set right product == 1 so we can multiply
            #also when it is empty space its basically a one
            right_product = 1
            #iterate again but this time starting from index +1 and until the end of nums
            for k in range(i + 1, len(nums)):
                #left product == left product * current num
                left_product = left_product * nums[k]

            #now to get the total product multiply both
            total = left_product * right_product
            #then update result everytime
            result[i] = total
        return result
            


        