class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return the k most frequent elemnts in list

        #keep track of the count in dictionary
        count = {}
        #keep track of the frequency in list
        frequency = []
        #iterate through nums and add that many spots +1 to include zero
        for i in range(len(nums) + 1):
            frequency.append([])
        print(frequency)
        #iterate through nums
        for num in nums:
            #update the value of count with how many times it shows
            #if it shows up in count add 1, or else let it be zero and add 1
            count[num] = 1 + count.get(num , 0)
        print(count)

        #iterate through count and get both numbers and count
        #.items gets both numbers and count
        for num, count in count.items():
            #frequency count to get appened with the num
            frequency[count].append(num)
        print(frequency)

        #now the results return list
        result = []
        #iterate through frequency from the back 
        for i in range(len(frequency) - 1, 0 , -1):
            #now get the actual index valyes
            for num in frequency[i]:
                #append num to result
                result.append(num)
                #when length of result == k return reuslt
                if len(result) == k:
                    return result






