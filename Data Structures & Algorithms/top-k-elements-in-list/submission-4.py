class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dictionary for keeping count
        count = {}
        #list to store the frequency
        frequency = []
        #for frequency iterate throug the amount thigns in nums and add that many +1 to include zero
        for i in range(len(nums) + 1):
            frequency.append([])
        print(frequency)

        #we want to get the frequency of our nums
        #iterate through nums
        for num in nums:
            #update the count so we do 1 + get(num,0)
            count[num] = 1 + count.get(num, 0)
        print(count)

        #iterate through both numbers and count use .item
        #this is to populate frequency 
        for num, count in count.items():
            #so now go into the frequency through count and then append the num 
            frequency[count].append(num)
        print(frequency)

        #results
        result = []
        #go through frequency from the back up to zero and go backwards
        for i in range(len(frequency) -1, 0 , -1):
            #then go through the frequency values
            for i in frequency[i]:
                #append this to result
                result.append(i)
                #once it equals k return result
                if len(result) == k:
                    return result

        
        
        