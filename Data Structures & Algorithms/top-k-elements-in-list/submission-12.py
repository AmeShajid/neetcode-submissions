class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return the numbers that appear the most and its equal to k
        
        #so we need to create our frequency 
        frequency = []
        #first iterate through our nums but make sure we add one so we can hold the number 0 
        for num in range(len(nums) + 1):
            #add empyty lists
            frequency.append([])
        print(frequency)

        #we need to create the count
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        print(count)            

        #we need to then populate frequency with our count
        #grab the number and count from count
        for number, count in count.items():
            #and then for the frequency count append the number there
            #so here we do the count then append the number to that one
            frequency[count].append(number)
        print(frequency)
        
        #now we need a result list
        result = []
        #iterate through frequency
        for bucket in range(len(frequency) -1, 0, -1):
            for num in frequency[bucket]:
                result.append(num)
                if len(result) == k:
                    return result
                