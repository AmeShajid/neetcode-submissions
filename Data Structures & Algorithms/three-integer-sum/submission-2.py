class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #first we need to store this in a list
        result = []
        #then we need to sort everything so its easier to handle the duplciates
        nums.sort()
        #now we need to iterate with both index and value
        for index, value in enumerate(nums):
            #we want to make sure the we dont grab the same number twice
            #so when the index is after the first number AND
            #we need to make sure the value previoud is NOT equal to value from the previus one
            if index > 0 and value == nums[index-1]:
                #we continue cause we know its not a duplcuiate
                continue
            
            #now start the pointers
            #left is going to index + 1 because we are already lopping
            left = index + 1
            right = len(nums) - 1

            #now loop make sure they dont cross paths
            while left < right:
                #now get the threesum total
                threesum = value + nums[left] + nums[right]

                #now if our threesum is greater than 0 we need to go back one from the right because we need to make sure everythign eqal 0
                if threesum > 0:
                    right -= 1
                
                #vice versa for opp
                elif threesum < 0:
                    left += 1
                
                #now if it gets past both that means its equal which then we add it to the result
                else:
                    result.append([value, nums[left], nums[right]])
                    #then we conmtinue going so go left once forget right leave tyhat the same
                    left += 1
                    #so now weneed to make susre we still dont find any duplciates
                    #so while we are still lopping and 
                    #if our left and the previous number are the same then just cojntinue moving
                    while left < right and nums[left] == nums[left -1 ]:
                        left += 1
        return result
        