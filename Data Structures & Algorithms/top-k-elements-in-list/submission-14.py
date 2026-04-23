class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first we need to get a frequency of the amount of numbers in the list also do + 1 to include 0 
        #iterate through nums
        frequency = []
        for num in range(len(nums) + 1):

            frequency.append([])
        print(frequency)

        #then we need to get a count for how many numbers show up each time
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        print(count)

        #so now with the count we need to populate the frequency 
        for number, value in count.items():
            frequency[value].append(number)
        print(frequency)

        #then we need to create our result 
        result = []
        for bucket in range(len(frequency) -1, 0, -1):
            for number in frequency[bucket]:
                result.append(number)
                if len(result) == k:
                    return result