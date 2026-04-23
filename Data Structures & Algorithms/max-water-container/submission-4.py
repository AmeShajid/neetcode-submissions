class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #since we are returning an int we need to hold result as a 0
        result = 0

        #now we need to set our pointers
        left = 0
        right = len(heights) - 1

        #now loop until they cross
        while left < right:
            #so now we need to do the area formula
            #first we need to get the width which is just widtrh = right - left
            width = right-left
            #now we need to get the hight
            #the height is going to be the minimum becasue we need to make like a cointair
            height = min(heights[left], heights[right])
            #then calculate the formula
            area = width * height

            #so now we need to update resultr with eitther the new result or area take the max between the boith
            result = max(result, area)

            #so now we have to decided which one to move, we need to mvoe the shorter one
            if heights[left] < heights[right]:
                #since left is shorter then + 1
                left += 1
            else:
                #else we need to subrtact one so we can move towards teh moddile 
                right -= 1
        return result