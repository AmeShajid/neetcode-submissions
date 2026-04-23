class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #first we need to store our result
        result = []
        #then we need to sort our list
        nums.sort()
        #now we need to iterate through everything but with index and value
        for index, value in enumerate(nums):
            #so now we want to make sure that when we start looping we dont grab the same number twice yk
            #so go to the next index and then get the same value
            if index > 0 and value == nums[index -1]:
                continue
            #now we need to start our pointers
            #our left starts index + 1 because we already start with index and value
            left = index + 1
            #then right at the end
            right = len(nums) - 1

            #now loop it to make sure we dont cross paths
            while left < right:
                #now our three sum == value + nums[left] + nums[right]
                threesum = value + nums[left] + nums[right]
                #if our threesum value is bigger than 0 then go backwards from right because its smaller numbers
                if threesum > 0:
                    right -= 1
                #now if its too small then we go left + 1 becuase those are bigger nubmers
                elif threesum < 0:
                    left += 1
                #else its right and we add it
                else:
                    result.append([value, nums[left], nums[right]])
                    #then we continue this 
                    left += 1
                    #and now we want to amke sure we dont have any duplcates for the left value 
                    #continue without breaking loop
                    #and if new left  equal previous left then add another one
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return result



            
        