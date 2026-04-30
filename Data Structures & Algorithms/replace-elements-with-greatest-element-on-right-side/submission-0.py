class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #go through array from right to left
        #keep track of max value seen so far 
        #replace ach element with the max 

        #set the max right value to -1 
        max_right = -1
 
        #iterate through list from the end, to -1, going backwards
        for i in range(len(arr) -1, -1, -1):
            #set a current var to the current i 
            current = arr[i]
            #the current i set it to max right 
            arr[i] = max_right
            #for max right get the max between (max right, current)
            max_right = max(max_right, current)
        #return arr 
        return arr


        