class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create an empty dictionary to store the numbers
        numDict = {}
        
        # Add each number from the list into the dictionary
        for num in nums:
            numDict[num] = num
        
        # Variable to keep track of the longest sequence found
        longest = 0
        
        # Go through each number in the list
        for num in nums:
            # Check if the number is the start of a sequence
            if (num - 1) not in numDict:
                # Start counting the length of the sequence
                current = num
                length = 1
                
                # Keep checking if the next number exists
                while (current + 1) in numDict:
                    current += 1
                    length += 1
                
                # Update the longest sequence if needed
                longest = max(longest, length)
        
        # Return the longest sequence length
        return longest

