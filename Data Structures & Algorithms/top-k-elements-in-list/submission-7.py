class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first we need to get the count of the numbers
        count = {}

        #second we need to get the frequency of the numbers to store them
        frequency = []
        #we need to make similar amount of buckets for each frequency
        for i in range(len(nums) + 1):
            frequency.append([])
        print(frequency)

        #now we need to populate the count
        for num in nums:
            #access the num add 1 to the number if we dont have it make it zero
            count[num] = 1 + count.get(num, 0)
        print(count)

        #now we need to populate the frequency
        for number, count in count.items():
            frequency[count].append(number)
        print(frequency)

        #now the result
        result = []
        for i in range(len(frequency) -1, 0 ,-1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result


                
    
        