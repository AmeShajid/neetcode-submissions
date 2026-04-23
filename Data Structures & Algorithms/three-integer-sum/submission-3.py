class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #goal: all 3 have to equal 0 
        #so first we need to store everything in a list
        result = []
        #then we need to sort everythign
        nums.sort()

        #then we need to iterate with index and valyue
        for index, value in enumerate(nums):
            #we need to make sure we skip duplciates
            #duplicates are valid when index > 0 and if our value is the same as previous value
            #if we see a duplicate then just contrinue with the loop skip evrythign under
            if index > 0 and value == nums[index - 1]:
                continue
            
            #now start our pointers
            #we go left = index +1 because we already ahve one value which is the valeu from the loop
            left = index + 1
            #right is just regular len(nums) - 1
            right = len(nums) -1 

            #so now start our while loop
            while left < right:
                #now our threesum is all three added together
                threesum = value + nums[left] + nums[right]
                #so now if its greater than 0  from right -1 
                if threesum > 0:
                    right -= 1
                #elif its less than 0 left +1
                elif threesum < 0:
                    left += 1
                #else that means its match so add this to result by appening the list
                else: 
                    result.append([value, nums[left], nums[right]])
                    #now we need to continue 
                    left += 1
                    #so continye the loop and make sure left value doesnt equal left -1
                    while left<right and nums[left] == nums[left -1]:
                        #if thats the case just left +1 and contrinyue
                        left += 1
        return result
        