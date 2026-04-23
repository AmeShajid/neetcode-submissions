class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #return the indixes that are in a ones based so that means +1 to all index values
        #return the index values that equal the target

        #set up two pointers 
        #one for the first value
        i = 0
        #one for the ending value 
        j = len(numbers) - 1

        #so now we want to keep checking while i < j thisis so theres no overlap
        while i < j:
            #keep track of the current total
            sum = numbers[i] + numbers[j]
            #here are our conditions

            #if our sum is greater than the target then 
            if sum > target:
                #move our right point -1
                j -= 1
            #if our sum is less than our target
            elif sum < target:
                i += 1
            #else is is correct
            else:
                #return in a list index values plus one
                return[i + 1, j +1]
        return []

