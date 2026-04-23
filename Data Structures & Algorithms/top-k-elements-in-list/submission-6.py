class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #approach 
        #First populate frequency
        #then populate count
        #then iterate through frequency
        
        #first we need to have a storage for count
        count = {}

        #then we need a list for the frequency 
        frequency = []
        #we need to populate the frequency with teh same amount of numbers as the list but +1 to include zero
        for i in range(len(nums) + 1):
            frequency.append([])
        print(frequency)

        #we need to first get the frequency of our nums
        #iterate through nums
        for num in nums:
            #update the count for the num with the actual count of it
            #count.get will get the value if theres no value its 0 +1 if theres already a value then its going to add that amount plus one
            count[num] = 1 + count.get(num, 0)
        print(count)

        #iterate through both numbers and count so we use .items
        #basically since we have a pair in our dictionary we use .items to get both numbers
        for num, count in count.items():
            #now go into the frequency for count append the number
            frequency[count].append(num)
        print(frequency)

        #iterate through this and get the k back
        result = []
        for i in range(len(frequency) -1, 0, -1):
            #access teh frequency values
            for n in frequency[i]:
                #append to result
                result.append(n)
                #when len(result) == k return results
                if len(result) == k:
                    return result

        

        
        
        