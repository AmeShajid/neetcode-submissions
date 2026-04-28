class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency  = []

        #first we need to make a list with the amount of items we have + 1 for 0
        for i in range(len(nums) + 1):
            frequency .append([])
        print(frequency )

        #second we need to make a frequency dictionary 
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        print(count)

        #third we need to put the frequency inside of the population list
        for index, value in count.items(): 
            frequency[value].append(index)
        print(frequency )

        result = []
        #now iterate backwards and make sure we can return the 2most 
        for bucket in range(len(frequency)-1, 0 ,-1):
            for number in frequency[bucket]:
                result.append(number)
                if len(result) == k:
                    return result