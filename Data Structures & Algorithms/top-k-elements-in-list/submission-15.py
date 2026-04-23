class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first we need to create a list with just the amount of len + 1 so we can the 0 as well
        frequency_storage = []
        for num in range(len(nums) + 1):
            frequency_storage.append([])
        print(frequency_storage)

        #so now we need to get the counts in the dictionary 
        count = {}
        #iterate and fill the count 
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        print(count)

        #now fill the frequency
        for number, value in count.items():
            frequency_storage[value].append(number)
        print(frequency_storage)

        #so now we need to actually return the number
        result = []
        for bucket in range(len(frequency_storage)-1 , 0, -1):
            #enter the bucket 
            for number in frequency_storage[bucket]:
                result.append(number)
                if len(result) == k:
                    return result
        