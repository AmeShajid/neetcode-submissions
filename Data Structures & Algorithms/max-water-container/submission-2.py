class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1. Start with no water (result is 0)
        result = 0

        # 2. Put two fingers: one at the start (left), one at the end (right)
        left = 0
        right = len(heights) - 1

        # 3. Move the fingers toward each other
        while left < right:
            # 4. Calculate the area between left and right bars
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height

            # 5. Update the result if this area is bigger than what we have seen
            result = max(result, area)

            # 6. Move the smaller bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result