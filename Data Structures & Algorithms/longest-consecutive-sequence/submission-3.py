class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #first we need to store the numbers
        storage = {}
        #then we need to fill  this storage with all the nums
        for num in nums:
            #just make it equal to num cause thats what we are checkingh for
            storage[num] = num
        
        #now start our longest count right here
        longest = 0

        #iterate through nums
        for num in nums:
            #$now we need to check to see if the previous number is in num
            if (num -1) not in nums:
                #change the current number to right one
                current = num
                #also now I want to add 
                length = 1
                #now we continue until we are done
                while (current + 1) in storage:
                    current += 1
                    length += 1
                #so now update longedst with the max
                longest = max(longest, length)
        return longest

        