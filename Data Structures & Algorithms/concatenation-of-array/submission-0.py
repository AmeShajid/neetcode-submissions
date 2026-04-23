class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        #time - o(n) - its a 2n operation so just drop 2 and its n
        #space - o(n) - grows up input size
 
        #have a new list for holding
        new_list = []
        #iterate through this twice
        for i in range(2):
            #npw iterate through nums
            for num in nums:
                #append it to the new list
                new_list.append(num)
        #return new list
        return new_list
        