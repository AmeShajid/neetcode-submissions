class Solution:
    def trap(self, height: List[int]) -> int:
        #return max area that can we held in between each one
        #first it there is no height just return 0
        if not height:
            return 0

        #start our two pointers
        left = 0
        right = len(height) -1

        #now we have to store our maxes
        leftmax = height[left]
        rightmax = height[right]

        #we need to store total amount store
        result = 0

        #loop until they cross
        while left < right:
            #if our leftmax is less than right then we want to move left one one
            if leftmax < rightmax:
                #move left one
                left += 1
                #change the leftmax now see if theres naother new max
                leftmax = max(leftmax, height[left])
                #update our rsult to see if theres nay water trapped
                result += leftmax - height[left]
            #now we have to check vice versa
            else:
                #if our rightmax is less than our leftmax
                right -= 1
                #now we have to updat eour rightmax
                rightmax = max(rightmax, height[right])
                #update reuslt
                result += rightmax - height[right]
        return result
        