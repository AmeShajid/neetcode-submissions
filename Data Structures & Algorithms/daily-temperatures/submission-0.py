class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create a list to store the answer for each day
        answer = [0] * len(temperatures)

        # This stack will keep track of indexes of temperatures we're waiting on
        stack = []  # We'll store indexes here, not actual temps

        # Go through each temperature
        for today in range(len(temperatures)):

            # While the stack is not empty and today's temp is warmer than the temp at the top index in the stack
            #temperatures[stack[-1]] is just going to the end of the stack then going to the index of that temperateure value
            while stack and temperatures[today] > temperatures[stack[-1]]:
                previous_day = stack.pop()  # Get the previous day we were waiting on
                # Calculate how many days it took to get warmer
                answer[previous_day] = today - previous_day

            # Add today's index to the stack to wait for a warmer day
            stack.append(today)

        return answer


        