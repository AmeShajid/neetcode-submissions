class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first we need to store the count
        count = {}

        #second we need to keep track of frequency
        frequency = []
        #we ned to populate frequency with the amount of numbers there are
        for i in range(len(nums) +1):
            frequency.append([])
        print(frequency)

        #we need to populate count first
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(count)

        #we need to populate frequency
        for num, count in count.items():
            frequency[count].append(num)
        print(frequency)

        #now the result
        result = []
        #iterate through frequency
        for i in range(len(frequency) -1, 0 , -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result
