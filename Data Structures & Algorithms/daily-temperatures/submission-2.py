class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result list filled with 0s (same length as temperatures)
        result = [0] * len(temperatures)

        # stack to store indices of temperatures (monotonic decreasing stack)
        stack = []

        # loop through each day
        for i, temp in enumerate(temperatures):
            # check if current temp is warmer than the last in the stack
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()  # get the previous day index
                result[prev_day] = i - prev_day  # days waited
            stack.append(i)  # push current day index

        return result

        