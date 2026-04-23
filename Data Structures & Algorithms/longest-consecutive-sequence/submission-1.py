class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #first we need to store all of these values
        numdict = {}

        #then add all of the numbers inside of nums
        for num in nums:
            numdict[num] = num

        #start a length for the longest
        longest = 0

        #first iterate through nums
        for num in nums:
            #now we need to check if the num-1 is in our dicitonary
            if (num-1) not in numdict:
                #start the count for the longet length and make the current that num
                current = num
                length = 1

                #now keep checkign every one after if its in it
                while (current + 1) in numdict:
                    current += 1
                    length += 1

                #update the longest sequence and get the max
                longest = max(longest, length)
        #return the longest sequecne
        return longest
        