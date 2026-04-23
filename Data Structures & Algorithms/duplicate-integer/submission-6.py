class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Return True if value appears more than once in array
        #Return False if all values appear once in array

        #Dictionary to store all the seen values
        check = {}
        #Iterate through all numbers in nums
        for num in nums:
        #if number is in dictionary return True
            if num in check:
                return True
        #else add the value to the dictionary make the value = 1 
            else:
                check[num] = 1
        #return False
        return False

