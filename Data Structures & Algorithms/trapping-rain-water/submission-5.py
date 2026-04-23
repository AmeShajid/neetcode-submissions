class Solution:
    def trap(self, height: List[int]) -> int:

        #first check if the height is 0
        if not height:
            return 0

        #start our left and right poitners
        left = 0
        right = len(height) -1

        #create brand new current left/right maxes
        leftmax = height[left]
        rightmax = height[right]

        #create a result var
        result = 0 

        #start loop
        while left < right:

            #if the left max less than rigth amx
            if leftmax < rightmax:
                #left + 1
                left += 1
                #update curretn left max with leftmnax or height left
                leftmax = max(leftmax, height[left])
                #result left max - high left 
                result += leftmax-height[left]
            
            #else
            else:
                #do this for the right 
                right -= 1
                rightmax = max(rightmax, height[right])
                result += rightmax-height[right]
                #return result
        return result
        