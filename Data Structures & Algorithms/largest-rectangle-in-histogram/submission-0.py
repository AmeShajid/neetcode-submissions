class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Add a zero at the end so every bar gets handled
        heights.append(0)
        # Stack to keep indices of the bars
        stack = []
        max_area = 0

        for i in range(len(heights)):
            # While the stack isn't empty and this bar is shorter than the last one in the stack
            while stack and heights[i] < heights[stack[-1]]:
                # Pop the last bar's index from the stack
                top_index = stack.pop()
                height = heights[top_index]
                # If the stack is empty, width is i
                if not stack:
                    width = i
                else:
                    # Else, width is between this bar and the bar before the popped one
                    width = i - stack[-1] - 1
                # Calculate area
                area = height * width
                # Update max_area if this is the biggest so far
                if area > max_area:
                    max_area = area
            # Add the current bar's index to the stack
            stack.append(i)
        return max_area