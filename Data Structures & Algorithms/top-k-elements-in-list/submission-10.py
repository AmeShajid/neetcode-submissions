class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first we need to create a frequency list
        frequency = []
        for num in range(len(nums) + 1):
            frequency.append([])
        print(frequency)

        #then we need to get a count
        #fill the dict with tthe counts of each number
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        print(count)
        
        #now we need to populate frequency with count
        for num, count in count.items():
            frequency[count].append(num)
        print(frequency)

        #now result
        result = []
        for i in range(len(frequency) -1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result