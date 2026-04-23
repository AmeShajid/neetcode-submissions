class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        #I want to iterate through each number in temp and find the same number
        for num in nums:
            # num = 1, check if num is in temp
            if num in temp:
                return True
            else:
                temp.append(num)
        return False  


        #  nums = [1, 2, 3, 3] temp = []
        # num = 1 temp = [1] 
        #num = 2 temp = [1,2] 
        # num = 3 temp = [1,2,3] 
        #num = 3 = temp [1,2,3] dup found return True
         