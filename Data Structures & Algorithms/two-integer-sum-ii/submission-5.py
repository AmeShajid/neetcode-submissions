class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #left pointer
        left = 0
        #right pointer
        right = len(numbers) - 1

        #enumerate values index and value
        for index, value in enumerate(numbers):
            #get total by combining numbers left + numbers right
            total = numbers[left] + numbers[right]
            #if total greater than target
            if total > target:
                #- 1
                right -= 1
            #elif total less than target
            elif total < target:
                #+ 1
                left += 1
            #else
            else:
                #return in a list left + 1 , right + 1
                return [left +1, right +1]
        #return list 
        return []
        