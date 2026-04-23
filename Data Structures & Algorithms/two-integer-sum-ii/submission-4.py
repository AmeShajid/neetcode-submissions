class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #start a left and a right pointer
        left = 0
        right = len(numbers) - 1

        #iterate through nums with both index and value
        for index, value in enumerate(numbers):
            #calculate the total number
            total = numbers[left] + numbers[right]
            #so now we need to to see if its greater than or equal to the target
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                #that means we found it
                return [left + 1, right + 1]
        return []
        