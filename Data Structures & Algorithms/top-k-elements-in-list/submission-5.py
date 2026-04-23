class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first populate frequency
        #then populate count
        #then iterate through frequency

        #count for storage
        count = {}
        #list for frequency
        frequency = []
        #populate frequency with the amount of nums
        for i in range(len(nums) + 1):
            frequency.append([])
        print(frequency)

        #populate frequency
        #iterate through nums
        for num in nums:
            #access count 
            count[num] = 1 + count.get(num, 0)
        print(count)

        #then populate frequency with count
        #iteate through count with both num and count
        for num, count in count.items():
            #populate frequency count with the num
            frequency[count].append(num)
        print(frequency)

        #iterate through this and get the k back
        #get result
        result = []
        for i in range(len(frequency) -1, 0 , -1):
            #access the frequency values
            for i in frequency[i]:
                #append to result
                result.append(i)
                #when it == k return the result
                if len(result) == k:
                    return result




