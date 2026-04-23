class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return True if value is in more than once
        #return False if value is not in more than once

        check = []

        #iterate through nums
        for num in nums:
            #check if num is in check 
            if num in check:
                return True
            #if not then append
            else:
                check.append(num)
        return False

        """
        nums = [1,2,3,3] check =[]
        if 1 in check check , 1

        """

         