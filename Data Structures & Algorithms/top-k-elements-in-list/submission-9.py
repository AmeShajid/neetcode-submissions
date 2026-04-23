class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #first populate frequency
        #we need a frequency list to keep track of how many times a number pops up also do +1 so we can include zero
        frequency = []
        for num in range(len(nums) + 1):
            frequency.append([])
        print(frequency)    

        #second populate count
        #now we need to get the count of each number how many times it shows up
        #store this in a dictionary
        count = {}
        #iterate through number
        for num in nums:
            #account count= 1 + get the number if its not in the diciontary make it zero
            count[num] = 1 + count.get(num, 0)
        print(count)

        #third populate frequency with numbers
        #first get the num and the count of the num from count dict
        for num, count in count.items():
            #access the count bubble in ferquency and append the number
            frequency[count].append(num)
        print(frequency)

        #fourth get the result
        #store the results in a list so we can return the list
        result = []
        #iterate through frequency starting from the back until we reach 0 and go backwards
        for i in range(len(frequency) -1, 0, -1):
            #now access each box in frequency
            for n in frequency[i]:
                #add this to result
                result.append(n)
                #once this == our k value return result
                if len(result) == k:
                    return result

