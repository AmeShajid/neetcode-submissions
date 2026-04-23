class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #first create a storage with all of our nums inside of it
        storage = {}
        for num in nums:
            storage[num] = 1
        print(storage)
        
        #okay so now we need to iterate through nums until we get the longest consecutive sequence
        #so start your longest 
        longest = 0 
        #iterate through nums
        for num in nums:
            #so now check if the current number -1 is in our storgae
            if (num -1) not in storage:
                #if its not in there then our current is our ongest 
                current = num
                #start out length tracker
                length = 1
                #so now we just keep iterating until we run out so do a while
                while current + 1 in storage:
                    current += 1
                    length += 1
                #so now we need to update longest
                longest = max(longest, length)
        return longest