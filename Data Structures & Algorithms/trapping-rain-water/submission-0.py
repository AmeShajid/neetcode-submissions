class Solution:
    def trap(self, height: List[int]) -> int:
        
        # if height list is empty, return 0 because no water can be trapped
        if not height:
            return 0
        
        # pointers starting from both ends
        left = 0
        right = len(height) - 1

        # leftMax stores the highest bar seen from the left so far
        leftMax = height[left]
        # rightMax stores the highest bar seen from the right so far
        rightMax = height[right]

        # result will store total amount of trapped water
        result = 0

        # loop until left and right pointers meet
        while left < right:
            # if leftMax is smaller, we move left pointer
            if leftMax < rightMax:
                left += 1  # move left pointer to the right
                leftMax = max(leftMax, height[left])  # update leftMax if needed
                result += leftMax - height[left]  # water trapped at this position
            else:
                right -= 1  # move right pointer to the left
                rightMax = max(rightMax, height[right])  # update rightMax if needed
                result += rightMax - height[right]  # water trapped at this position
                
        # return the total trapped water
        return result


        