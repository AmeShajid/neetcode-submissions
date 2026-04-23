class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Find all unique triplets that == 0
            #nums[i] + nums[j] +nums[k] = 0
            #i j k all have to be different index values
            #each triplet must be unique no duplicates

            #first we need to store the result in a list
            res = []
            #then first we want to sort the list to make the logic easier
            nums.sort()

            #now we want to loop through the list do enumerate do grab index and value
            for index, value in enumerate(nums):

                #when we go past our first index value
                #if the value is the same as the previous index then just continue
                #we want to skip it
                if index > 0 and value == nums[index - 1]:
                    continue

                #set our two pointers
                #left is going to be index+1 
                left = index + 1

                #right is going to be from the ending
                right = len(nums) - 1

                #while our left is < right
                while left < right:
                    #add all three values together
                    threesum = value + nums[left] + nums[right]

                    #if our sum is greater than 0 than from the right go back one
                    if threesum > 0:
                        right -= 1

                    #if our sum is less than 0 then from the left go up 1
                    elif threesum < 0:
                        left += 1

                    #else its right append this to the result
                    else:
                        #append ina list format
                        res.append([value, nums[left], nums[right]])

                        #move the left pointer 
                        left += 1

                        #skip teh duplciates for the left value
                        while left < right and nums[left] == nums[left -1]:
                            left += 1
            return res



