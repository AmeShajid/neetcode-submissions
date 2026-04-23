class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a freq list
        frequency = []
        #populate freq list iterate through nums with +1 to include 0
        for num in range(len(nums) + 1):
            #each position append a list
            frequency.append([])
        #print list
        print(frequency)

        #count storage
        count = {}

        #populate count 
        for num in nums:
            #if num in count add 1 
            if num in count:
                count[num] += 1
            #else add it
            else:
                count[num] = 1
        print(count)        

        #now we need to populate freq
        for number, value in count.items():
            #populate freq
            frequency[value].append(number)
        print(frequency)

        #now we need to access and get the top 2
        #hold in a result
        result = []
        #iterate through 
        for bucket in range (len(frequency) -1, 0, -1):
            #access the buckets 
            for number in frequency[bucket]:
                result.append(number)
                if len(result) == k:
                    return result
