class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #find the max amunt of water this thing can hold
        #store our result 
        result = 0

        #now we need to set our pointers
        left = 0
        right = len(heights) - 1

        #now loop until they cross
        while left < right:
            #now we just need to do the basic area formula
            width = right - left
            #take the minimum between the max might cause the water to spill 
            height = min(heights[left], heights[right])
            area = width * height 

            #now to update our result we want to just see whats bigger our result or the area we caluclate
            result = max(result, area)

            #then if our left heigh is smaller than our right heigh then go up one or decrease one
            #we want to move the smaller bar because then we can eventually find the tall ones
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result
            
        