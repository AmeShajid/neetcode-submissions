class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #have a current count of 1s
        count = 0
        #have a maxc count to rmrm streak
        max_count = 0

        #iterate through nums with range
        for i in range(len(nums)):
            #if nums i == 1
            if nums[i] == 1:
                #add 1 to count
                count += 1
                #update max count if count is bigger
                max_count = max(max_count, count)
            #else
            else:
                #reset count to 0
                count = 0
        return max_count
        