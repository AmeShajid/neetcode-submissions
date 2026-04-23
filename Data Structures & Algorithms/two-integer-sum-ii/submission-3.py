class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #set up a left and right pointer
        left = 0
        right = len(numbers) - 1

        #loop through numbers until the end
        while left < right:
            #add current numbers up 
            total = numbers[left] + numbers[right]

            #check if the total is greater than target
            if total > target:
                right -= 1
            #else if that means total < target
            elif total < target:
                #do elft + 1
                left += 1
            #its right and we just need to return with + 1 index
            else:
                return [left + 1, right + 1]
        #if everything fails just return none
        return []
            


        