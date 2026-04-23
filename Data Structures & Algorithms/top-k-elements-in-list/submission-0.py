class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    #return the values that return the most

   
    #Approach:
    #list  = [1,1,1,2,2,3]

    #i (how many times shown up + len(list)) : 0 , 1 , 2 , 3 , 4 , 5 , 6
    #values : blank , [3] , [2], [1]
        
        #Dictionary for keep track of count
        count = {}

        #anotehr list to keep track of the frequency of the list +1 because you have to include 0
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])

        #now count over each number in nums
        #iterate through number
        for num in nums:
            #if num is in count take its value and add one
            #if num not in count use 0 and add 1
            count[num] = 1 + count.get(num, 0)
        
        #organizing by frequency
        #we grab both number and count with .items
        for num, cnt in count.items():
            freq[cnt].append(num)

        #now the resutl return in a list
        res = []
        #iterate through list from the ending end at zero and move back 1 spot at a time
        for i in range(len(freq) -1 , 0 , -1):
            #iteate through freq and through all of them
            for num in freq[i]:
                #appened to res
                res.append(num)
                #once our res == k then return
                if len(res) == k:
                    return res















        