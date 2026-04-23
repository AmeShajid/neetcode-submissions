class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first we need to make a frequency list of all of the numbers, make sure we also inlucde 0
        frequency = []
        #iterate through all of them but with range to include zero so just add 1
        for number in range(len(nums) + 1):
            #add them to an empty list in  List
            frequency.append([])
        print(frequency)

        #so now we need to get the count of each number
        #so start a reagular count dic
        count = {}
        #iterate through nums
        for num in nums:
            #if number in count then make it add 1 
            if num in count:
                count[num] += 1
            #else make it equal 1 to the count
            else:
                count[num] = 1
        #print it out
        print(count)

        #so now we want to fill frequency with count but from the back 
        #so first enumerate number and the value in count
        for number, value in count.items():
            #in place of the value we have put the numer 
            frequency[value].append(number)
        print(frequency)

        #so now we need to get the result 
        #we have to return a result 
        result = []
        #so now what we want to do is iterate through frequency BUT from the back, until 0, go backwards
        for bucket in range(len(frequency) -1, 0, -1):
            #so now we need to access each nbumber in the bucket
            for number in frequency[bucket]:
                #append each numberr to result
                result.append(number)
                #so now if result == k then return result
                if len(result) == k:
                    return result

