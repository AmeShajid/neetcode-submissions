class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #we are returning a list
        #our result is going to be same len as temp but we will replace values
        result = [0] * len(temperatures)
        #our stack to keep track of values 
        #this will hold a pair: [temp, index]
        stack = []

        #now interate through temp with both index and value
        for index, value in enumerate(temperatures):
            #so we have to check if our stack is empty and if the current value is greater than what we have in our stack
            while stack and value > stack[-1][0]:
                #we want to pop that values
                stackValue,stackIndex  = stack.pop()
                #for the result whatevre the index of the temp is we need to find the number of days it took us to find
                #so to the current day (i) - the stackindex
                result[stackIndex] = index - stackIndex
            #after everything is done append ot the stack
            #jkust add the current value and the current index
            stack.append([value, index])
        #we dont have to fill in extra because we already have all 0s in it
        return result

        