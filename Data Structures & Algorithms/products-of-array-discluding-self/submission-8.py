class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first map all of the numbers with 1 and a len of nums
        result = [1] * len(nums)
        #iterate through nums with rnage
        for index in range(len(nums)):
            #start your leftproduct ehre = 1
            left_product = 1
            #so now iterate from 0 to current index
            for left_pointer in range(0, index):
                #left product is product * all of j values
                left_product *= nums[left_pointer]
            #do the same for right now 
            right_product = 1
            #iterate from i+1 to the len of nums
            for right_pointer in range(index+1, len(nums)):
                right_product *= nums[right_pointer]
            
            #now calculate the total product 
            total_product = right_product * left_product
            #update everything in result for every index value 
            result[index] = total_product
        return result