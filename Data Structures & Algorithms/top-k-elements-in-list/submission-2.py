class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dictionary for keeping count
        count = {}
        #list to store my frequency
        frequency = []
        #we want to create empty lists for every single num also +1 to include zero
        for i in range(len(nums) + 1):
            frequency.append([])
        print(frequency)

        #we want to get the frequency of our nums
        #iterate through nums
        for num in nums:
            #update the count
            #add 1 to the num value and theres nothing do 0
            count[num] = 1 + count.get(num,0)
        print(count)

        #iterate through count and get both numbers and count
        #.items gets both numbers and count
        for num, count in count.items():
            #frequency count to get appened with the num
            frequency[count].append(num)
        print(frequency)

        #we want the results
        result = []
        #iterate through frequency from the back
        for i in range(len(frequency) -1, 0, -1):
            for i in frequency[i]:
                #add this to num
                result.append(i)
                if len(result) == k:
                    return result

