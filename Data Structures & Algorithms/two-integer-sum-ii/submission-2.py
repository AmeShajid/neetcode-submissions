class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #so basically just return the numberes that equal to the target but its going to index + 1

        #first set up the pointers
        left = 0
        right = len(numbers) - 1

        #so now iterate until they meet
        while left < right:
            #so now we need to get the total of the target
            total = numbers[left] + numbers[right]

            #so now we need to cehck and make sure the total is correct 
            #if its greater -1 from the right
            if total > target:
                right -= 1
            #if its left +1 from the left
            elif total < target:
                left += 1
            #return the nubmers but +1 the indexes
            else:
                return [left + 1, right + 1]
        #thid wont get reached, but return this so somethign gets reutned instead of none
        return []