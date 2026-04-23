class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # True = In list more than once
        #False = In list once

        #set new list so we can comapre
        temp = []

        #iterate through all of nums
        for num in nums:
            #check if num is in temp
            if num in temp:
                return True
            #if not then append to the list and continue
            else:
                temp.append(num)
        return False
         