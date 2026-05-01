class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #first set a righht amx which is -1 
        max_right = -1

        #iterate through all arr but we need to go from the backside until the end so -1 
        for i in range(len(arr) -1, -1, -1):
            #set a current var to current arr index
            current = arr[i]
            #set current index to max right 
            arr[i] = max_right
            #update max right with current maxright to current
            max_right = max(max_right, current)
        #return arr
        return arr
        