class Solution:
    def trap(self, height: List[int]) -> int:
        #first check if the heigh is 0 
        if not height:
            #returnb 0
            return 0

        #create our left poitner
        left = 0
        #create our right poitner
        right = len(height) - 1

        #create our current leftmax
        leftmax = height[left]
        #create our current rightmax
        rightmax = height[right]

        #create result
        result = 0
        #start our while loop
        while left < right:
            #if leftmax > right max
            if leftmax < rightmax:
                #we want to move left + 1
                left += 1
                #update our current left max with either left max or current heigh[left]
                leftmax = max(leftmax, height[left])
                #update our result left max - current heigh
                result += leftmax - height[left]
            #else
            else:
                #repeat all of this for right
                right -= 1
                rightmax = max(rightmax, height[right])
                result += rightmax - height[right]
        return result