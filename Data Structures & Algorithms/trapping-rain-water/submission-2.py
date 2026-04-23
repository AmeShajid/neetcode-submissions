class Solution:
    def trap(self, height: List[int]) -> int:
        #if we cant trap any water then just return 0 
        if not height:
            return 0
        
        #set up our pointers
        left = 0
        right = len(height) - 1

        #we have to set the current maxes
        leftmax = height[left]
        rightmax = height[right]

        #since we are returning an int hold in a var
        result = 0

        #start the loop until they cross
        while left < right:
            #so if the leftmax is less tahn right max 
            if leftmax < rightmax:
                #we need to move left1 to make sure thats not the case
                left += 1
                #and then we need to get a new max
                leftmax = max(height[left], leftmax)
                #update the result to see if there any new water trapped
                result += leftmax - height[left]
            #else its teh opposite right is less tahn max
            else:
                #if right is less tahn left than we got -1
                right -= 1
                #get a new max fro rigth
                rightmax = max(rightmax, height[right])
                #than update rtesult
                result += rightmax - height[right]
        return result
        