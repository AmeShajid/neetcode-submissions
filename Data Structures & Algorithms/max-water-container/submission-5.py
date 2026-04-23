class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #first set a result \
        result = 0
        #next set out pointer
        left = 0
        right = len(heights) - 1
        #loop through until both meet
        while left < right:
            #create our width just right - left
            width = right - left
            #now we get out height right - left
            height = min(heights[right], heights[left])
            #now calculate the area width * height
            area = width * height
            #now update result with a max between area and result
            result = max(area, result)
            #now move the pointer that is less
            #check if left hieght is less than right height
            if heights[left] < heights[right]:
                #move left + 1 if its true
                left += 1
                #else move right -1 if false
            else:
                right -= 1
        #return result
        return result
        