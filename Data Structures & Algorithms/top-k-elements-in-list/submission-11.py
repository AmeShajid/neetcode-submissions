class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #first we need to get the frequency of the list
        frequency = []
        #we want to every possible frequency including the 0
        for num in range(len(nums) + 1):
            #appened empty []
            frequency.append([])
        print(frequency)

        #then we need to get a count of the list
        #we need to first store count and 
        #the amount each number has
        count = {}
        #iterate trhough nums
        for num in nums:
            #if its in the count then add 1
            if num in count:
                count[num] += 1
            #else add it to the count with a count of 1
            else:
                count[num] = 1
        print(count)

        #now we need to populate frequency with count
        #so get the index and value with .items
        for number, count in count.items():
            frequency[count].append(number)
        print(frequency)

        #now we need the result
        result = []
        #iterate through frequency starting from the back all teh way to 0 going backwards
        for i in range(len(frequency) -1, 0, -1):
            #now access the box INSIDE of frequency
            #frequency is a list with list inside of it
            for num in frequency[i]:
                #now append num to the result
                result.append(num)
                if len(result) == k:
                    return result
        