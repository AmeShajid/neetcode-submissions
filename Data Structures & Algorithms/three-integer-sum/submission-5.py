class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #need to find all unique triplets that sum to 0

        #storage is a list
        result = []
        #sort all the numbers so its easier 
        nums.sort()

        #iterate over all numbers 
        #we already have a base number we need
        for index, value in enumerate(nums):
            #need to skip duplicate numbers 
            if index > 0 and value == nums[index-1]:
                #continue
                continue
        
            #start pointers 
            #left we statr from the next positions 
            left = index + 1
            right = len(nums) - 1

            #start the loop
            while left < right:
                #get the total 
                threesum = value + nums[left] + nums[right]

                #if sum > 0
                if threesum > 0:
                    #right - 1
                    right -= 1
                
                #elif sum < 0:
                elif threesum < 0:
                    #left + 1
                    left += 1

                #else
                else:
                    #append these values to the result 
                    result.append([value, nums[left], nums[right]])
                    #move onto the next positions 
                    left += 1
                    #makesure to skip duplicates again 
                    while left < right and nums[left] == nums[left - 1]:
                        #and move left + 1
                        left += 1
            #return result
        return result
        
    