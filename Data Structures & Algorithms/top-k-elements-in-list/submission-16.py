class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #first we need to create a list with a position for all the nubmers 
        #create an empty list 
        frequency = []
        #iterate through the nums using range until the end and +1 for 0 
        for num in range(len(nums) + 1):
            #append an empty spot to the liust
            frequency.append([])
        #print the list
        print(frequency)

        #now we need to get the count for the amount of numbers we ahve 
        #create a couint dict
        count = {}
        #iterate through nums
        for num in nums:
            #if the number is in our dict 
            if num in count:
                #+1 to teh count
                count[num] += 1
            #else  
            else: 
                #its not in there and add a position 
                count[num] = 1
        #print dict 
        print(count)


        #so now we need to populate the frequency with the count
        #get both number and count from count
        for number, value in count.items():
            #popualte the frequency based on count with the number 
            frequency[value].append(number)
        #print that 
        print(frequency)

        #storage for result
        result = []

        #so now we need to return the k most value 
        #first iterate through the frequency but make sure its from the back to 0 going back wards
        for bucket in range(len(frequency) -1, 0, -1):
            #so now iterate inside of the bucket 
            for number in frequency[bucket]:
                result.append(number)
                if len(result) == k:
                    return result
                
        