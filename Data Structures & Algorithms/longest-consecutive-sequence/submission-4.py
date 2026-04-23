class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #so first we need to populate our storage with our nubmers
        storage = {}
        #iterate through and add our nums
        for num in nums:
            storage[num] = num

        #so now we need to check for our longest
        longest = 0 
        #iterate through nums
        for num in nums:
            #check if its in our storage the previous numbver
            if (num - 1) not in storage:
                #set our curent to this num
                current = num 
                #and also our length to 1
                length = 1
                #so now do a while until we are done
                while current + 1 in storage: 
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest