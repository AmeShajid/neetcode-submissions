class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #so store all the numbers in teh dictionary
        storage ={}
        #now add all the numbers to nums
        for num in nums:
            storage[num] = num
        
        #now start our longest count right here
        longest = 0

        #now we need to iterate trhough nums
        for num in nums:
            #now check if the previous number is in our dictionaryu
            if (num - 1) not in storage:
                #then change the current number to rigth now
                current = num
                #and change the length to 1
                length = 1
                #now while current + 1 is in our dicinotary
                while (current + 1) in storage:
                    #move both +1
                    current += 1
                    length +=1 
                #and update the length and longest
                #so everytime it runs through it can fidn that proper longest
                longest = max(longest, length)
        return longest


        