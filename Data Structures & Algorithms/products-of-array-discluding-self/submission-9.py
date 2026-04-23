class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first set a list with a value of 1 in each position 
        result = [1] * len(nums)
        #iterate through nums
        for i in range(len(nums)):
            #have a left counter and right counter == 1
            left_product = 1
            right_product = 1
            #iterate through current num until the i 
            for left_pointer in range(0 , i):
                #left counter multiply those positions by nym
                left_product *= nums[left_pointer]
            
            #iterate from current to the end of the list
            for right_pointer in range(i + 1, len(nums)):
                #rigth counter multiple those positive by current
                right_product *= nums[right_pointer]
            
            #your total == left * right 
            total_product = left_product * right_product

            #replace the value of each index with total product
            result[i] = total_product
        return result
        