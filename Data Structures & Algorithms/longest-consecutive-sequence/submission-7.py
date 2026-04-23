class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #first populate a storage with all the nums
        storage = {}
        for num in nums:
            storage[num] = 1

        #start a longest counter
        longest = 0
        #iterate through nums
        for num in nums:
            #if the curent num - 1 not in our storgae
            if (num -1) not in storage:
                #start our current num to num
                current = num
                #start our length pointer to 1
                length = 1
                #while our current + 1 in storage
                while current + 1 in storage:
                    #update our current and  length to += 1
                    current += 1
                    length += 1
                #now update longest between lognest and length
                longest = max(longest, length)
        #return longest
        return longest
        