class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we want to get teh max area between 2 bars
        #Basiaclly image the two bars are like a container filled with water cant overflow get the max

        #we want to keep our result somewhere so set it to zero
        result = 0

        #we need two pointers one from the left and right
        left = 0
        right = len(heights) - 1

        #mkaing sure the two pointers dont cross
        while left < right:
            #now do the area formula
            #in this case its (right - left) * min(left or right)
            #right - left is the distance between the bars width
            #the min is the height
            area = (right - left) * min(heights[left], heights[right])

            #onec we find the biggest area store it
            result = max(result, area)

            #now the condition
            #if our left is smllaer than our right then move that +1 vice versa
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result
    
            

        